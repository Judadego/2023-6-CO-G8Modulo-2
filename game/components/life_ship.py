from pygame.sprite import Sprite
import pygame

from game.utils.constants import LIFE,SCREEN_WIDTH,SCREEN_HEIGHT,SHIP_SPEED , SPACESHIP,SHIP_WIDTH,SHIP_HEIGHT,X_POS, Y_POS

class life_Spaceship():
    
    def __init__(self):
        self.image = LIFE 
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = 30
        self.rect.x = 40
        pass
    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
