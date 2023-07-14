
from pygame.sprite import Sprite
import pygame

from game.utils.constants import SCREEN_WIDTH,SHIP_SPEED , SPACESHIP,SHIP_WIDTH,SHIP_HEIGHT,X_POS,  Y_POS

class Spaceship(Sprite):

    def __init__(self) -> None:
        self.SHIP_WIDTH = SHIP_WIDTH
        self.SHIP_HEIGHT = SHIP_HEIGHT
        self.X_POS = X_POS
        self.Y_POS = Y_POS
        self.SHIP_SPEED = SHIP_SPEED
        self.image = SPACESHIP 
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH,self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.X_POS
        self.rect.x = self.Y_POS
    
    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
            
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
            
    def move_right(self):
        self.rect.x += self.SHIP_SPEED
    
    def move_up(self):
        self.rect.y -= self.SHIP_SPEED
    
    def move_down(self):
        self.rect.y += self.SHIP_SPEED