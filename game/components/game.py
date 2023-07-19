import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.spaceship import Spaceship
from game.components.life_ship import life_Spaceship
from game.components.bullet.bullet_manager import BulletManager
from game.components.menu import Menu

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.utils.constants import GAME_OVER , RESET_BUTTON

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
        self.game_over_image = GAME_OVER 
        self.game_over_image = pygame.transform.scale(self.game_over_image,(SCREEN_WIDTH/5,SCREEN_HEIGHT/5))
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.reset_button = RESET_BUTTON
        self.reset_button_rect = self.reset_button.get_rect(topright=(SCREEN_WIDTH - 20, 20))
        self.running = False
        self.death_score = 0
        self.score = 0
        self.menu = Menu('Press Any Key to start.....', self.screen)
        
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_reset_button(mouse_pos)

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.enemy_manager.update(self)
        self.check_collisions()

    def draw(self):
        """Draw the game objects, such as enemies, life, player, etc.
        """
        self.clock.tick(FPS)
        #self.screen.fill((255, 255, 255))
        if self.player.is_dead:
            self.screen.blit(self.game_over_image, self.game_over_rect)
            self.screen.blit(self.reset_button, self.reset_button_rect)
        else:
            self.draw_background()
            self.player.draw(self.screen)
            self.life.draw(self.screen)
            self.enemy_manager.draw(self.screen)
            self.bullet_manager.draw(self.screen,self)   
            self.draw_score()         
        pygame.display.flip()

    def draw_background(self):
        """Draw the background
        """
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
        
    def check_collisions(self):
        """Check if the frames collide
        """
        player_collision_area = pygame.Rect(self.player.rect.x + 10, self.player.rect.y + 10, 
                                    self.player.rect.width - 20, self.player.rect.height - 20)
    
        for enemy in self.enemy_manager.enemies:
             if player_collision_area.colliderect(enemy.rect):
              self.player.is_dead = True
              pygame.time.delay(2000)
              break        

    def check_reset_button(self, mouse_pos):
        if self.reset_button_rect.collidepoint(mouse_pos):
            # acciones necesarias para volver a empezar
            #  restablecer las posiciones de los objetos, puntajes, etc.
            self.reset_game()
            
    def reset_game(self):
        self.player.is_dead = False
        self.player.rect.x = SCREEN_WIDTH // 2
        self.player.rect.y = SCREEN_HEIGHT - 100
        self.enemy_manager.enemies.empty()
        self.bullet_manager.enemy_bullets.empty()
        self.bullet_manager.player_bullets.empty()

        self.playing = True
    
    
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_score > 0:
            self.menu.update_message("La tarea")
        icon = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon,(half_screen_width, half_screen_height))
        self.menu.draw(self.screen)
        self.menu.update(self)

    def update_score(self):
        self.score += 1

    def draw_score(self):
        pass