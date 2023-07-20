import pygame 
import random

from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1,ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH,MOVE_X,ENEMY_COLORS, KILL_ENEMY_SOUND
from game.utils.constants import SHIP_WIDTH,SHIP_HEIGHT,X_POS_E,Y_POS_E,SPEED_Y , SPEED_X , ENEMY_IMAGES
from game.components.bullet.bullet import Bullet

class Enemy(Sprite):
        
    def __init__(self, image=ENEMY_IMAGES[0], color=ENEMY_COLORS[3],speed_x = SPEED_X[0], speed_y = SPEED_Y[0], move_x_for = [30, 100]) -> None:
        super().__init__()
        self.original_image = image
        self.color = color
        self.image = self.original_image.copy()
        self.image.fill(self.color, special_flags = pygame.BLEND_RGB_MULT)
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(000, SCREEN_WIDTH - SHIP_WIDTH)  
        self.rect.y = random.randint(-200, -50)
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.movement_x = MOVE_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0],move_x_for[1])
        self.shooting_time = random.randint(30, 50)
        self.index = 0
        self.type = 'enemy'
        
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game)
        
        if self.movement_x == 'LEFT':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        
    def change_movement_x(self):
        self.index += 1 
        if ((self.index >= self.move_x_for and self.movement_x == 'RIGHT') or (self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH)):
            self.movement_x = 'LEFT'
            self.index = 0
        elif ((self.index >= self.move_x_for and self.movement_x == 'LEFT') or (self.rect.x <= 10)):
            self.movement_x = 'RIGHT'
            self.index = 0
            self.index=0
    
    def shoot(self, game):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            game.bullet_manager.add_bullet(bullet,game)
            self.shooting_time += random.randint(30, 70)
    

    
    