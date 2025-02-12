from game.persistence.save import read_data, save_data
import pygame
import os
from game.components.enemies.enemy_manager import EnemyManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.bullet.bullet_manager import BulletManager
from game.components.spaceship import Spaceship
from game.components.life_ship import life_Spaceship
from game.components.menu import Menu

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.utils.constants import GAME_OVER , RESET_BUTTON, FONT_STYLE, GAME_SOUND, GAME_OVER_SOUND
from game.utils.constants import INTRO

class Game:
    def __init__(self):
        pygame.init()
        #screen_info = pygame.display.Info()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.life = life_Spaceship()
        self.enemy_manager = EnemyManager()  
        self.bullet_manager = BulletManager() 
        self.power_up_manager = PowerUpManager()   
        self.game_over_image = GAME_OVER 
        self.game_over_image = pygame.transform.scale(self.game_over_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.reset_button = RESET_BUTTON
        self.reset_button_rect = self.reset_button.get_rect(topright=(SCREEN_WIDTH - 20, 20))
        self.running = False
        self.death_score = 0
        self.score = 0
        self.score_max = read_data()
        self.flag = 0
        self.cont = 0
        self.back_sound = GAME_SOUND
        self.game_over_sound = GAME_OVER_SOUND
        self.menu = Menu(' Press Any Key to start...', self.screen,self)
        self.data = read_data()
        self.level = 1 #añadir logica para subir de nivel
        
    def execute (self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                #implementar
        pygame.display.quit()
        pygame.quit()
        
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        user_input = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN  :
                mouse_pos = pygame.mouse.get_pos()
                self.check_reset_button(mouse_pos)
            #elif (user_input[pygame] and self.player.is_dead):
            #    self.reset_game()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.enemy_manager.update(self)
        self.power_up_manager.update(self)
        #self.check_collisions()                   #funcionalidad actualizada

    def draw(self):
        """Draw the game objects, such as enemies, life, player, etc.
        """
        self.clock.tick(FPS)
        #self.screen.fill((255, 255, 255))
        self.draw_background()
           
        if self.player.is_dead:
            if self.cont == 0 :
                pygame.mixer.Sound.play(self.game_over_sound)
                self.cont = 1
                self.save_data_score(self.score_max)
            self.draw_enemy_dead()
            self.screen.blit(self.game_over_image, self.game_over_rect)
            self.screen.blit(self.reset_button, self.reset_button_rect)
            
        else:
            self.player.draw(self.screen)
            if self.player.extra_life > 0:
                self.life.draw(self.screen)
                font = pygame.font.Font(FONT_STYLE, 50)
                text = font.render(f'X {self.player.extra_life} ', True, (255,255,255))
                self.screen.blit(text,(100,500))
            self.enemy_manager.draw(self.screen)
            self.bullet_manager.draw(self.screen,self)   
            self.power_up_manager.draw(self.screen)
            self.draw_power_up_time() 
        self.draw_score()  
        pygame.display.flip()

    def draw_background(self):
        """Draw the background
        """
        image = BG.copy()
        image.fill((255,255,255), special_flags = pygame.BLEND_RGB_MULT)
        image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
 
    def check_reset_button(self, mouse_pos):
        if self.reset_button_rect.collidepoint(mouse_pos) and self.player.is_dead:
            # acciones necesarias para volver a empezar
            #  restablecer las posiciones de los objetos, puntajes, etc.
            #self.show_menu()
            self.reset_game()
            
            
    def reset_game(self):
        self.player.is_dead = False
        self.player.rect.x = SCREEN_WIDTH // 2
        self.player.rect.y = SCREEN_HEIGHT - 100
        self.enemy_manager.enemies.empty()
        self.bullet_manager.enemy_bullets.empty()
        self.bullet_manager.player_bullets.empty()
        #self.power_up_manager.power_ups.empty()
        self.score = 0
        self.cont = 0
        self.player.has_power_up = False
        self.player.power_time_up = 0
        self.playing = True
        self.player.extra_life = 0
        self.enemy_manager.enemy_dead = 0
        self.enemy_manager.min_enemy = 2
        self.enemy_manager.max_enemy = 3
        self.record = 1000
    
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT - 200
        half_screen_width = SCREEN_WIDTH - 600
        self.menu.reset_screen_color(self.screen)
        #pygame.mixer.Sound.play(self.back_sound) #el audio se ejecuta muchas veces 
        #pygame.time.delay(2000)                  #al poner delay no deja correr el background
        icon = pygame.transform.scale(ICON, (70, 110))
        intro = pygame.transform.scale(INTRO, (829, 262))
        self.screen.blit(intro,(half_screen_width -350, half_screen_height - 400 ))
        self.screen.blit(icon,(half_screen_width, half_screen_height))
        self.menu.draw(self.screen)
        self.menu.update(self)

    def update_score(self,score):
        self.score += score
        if self.score_max['score'] < self.score:
           self.score_max['score'] = self.score                       #actualizamos el maxmio escore

    def draw_score(self):
        score = self.score_max['score']
        score_max_text = self.menu.font.render(f'Max Score: {score}', True, (250,250,250))
        self.screen.blit(score_max_text, (10, 10))
        if self.flag == 0:
           score_text = self.menu.font.render(f'Score: {self.score}', True, (250,250,250))
           self.screen.blit(score_text, (10, 60))

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 50)
                text = font.render(f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                text_rect = text.get_rect()
                self.screen.blit(text,(10,120))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
        if self.power_up_manager.double_active:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 50)
                text = font.render(f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                text_rect = text.get_rect()
                self.screen.blit(text,(10,150))
            else:
                self.power_up_manager.double_active = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
        
    def draw_enemy_dead(self):
        #enemies_kill = int(self.score / SCORE) 
        enemies_kill = self.enemy_manager.enemy_dead
        score_max_text = self.menu.font.render(f'You have deleted { enemies_kill } enemies.', True, (250,250,250))
        self.screen.blit(score_max_text, (300, 350))

    def save_data_score(self, score_max): 
        """Comprueba el score max actual con el almacenado en score.json

        Args:
            score_max (dict): dict 

        Returns:
            Null
        """
        datos = read_data()
        if datos['score'] < score_max['score']:            
            save_data(score_max)