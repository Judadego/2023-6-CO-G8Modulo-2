import random
import pygame 
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH,MOVE_X
from game.utils.constants import SHIP_WIDTH,SHIP_HEIGHT,X_POS,Y_POS,SPEED_Y , SPEED_X  

class Enemy(Sprite):
        
    def __init__(self) -> None:
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = X_POS[random.randint(0,10)]
        self.rect.y = Y_POS
        self.speed_y = SPEED_Y
        self.speed_x = SPEED_X
        self.movement_x = MOVE_X[random.randint(0,1)]
        self.move_x_for = random.randint(30,100)
        self.index = 0
        
    def update(self, ships):
        self.rect.y += self.speed_y

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
    
    