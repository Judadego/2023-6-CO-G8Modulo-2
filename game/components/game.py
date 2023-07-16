import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.spaceship import Spaceship
from game.components.life_ship import life_Spaceship

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.utils.constants import GAME_OVER 

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
        self.game_over_image = GAME_OVER 
        self.game_over_image = pygame.transform.scale(self.game_over_image,(SCREEN_WIDTH/5,SCREEN_HEIGHT/5))
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

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

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_manager.update()
        self.check_collisions()

    def draw(self):
        """Draw the game objects, such as enemies, life, player, etc.
        """
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        if self.player.is_dead:
            self.screen.blit(self.game_over_image, self.game_over_rect)
        else:
            self.draw_background()
            self.player.draw(self.screen)
            self.life.draw(self.screen)
            self.enemy_manager.draw(self.screen)
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
        for enemy in self.enemy_manager.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.player.is_dead = True
                break
