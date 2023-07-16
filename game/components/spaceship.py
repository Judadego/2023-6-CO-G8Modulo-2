
from pygame.sprite import Sprite
import pygame

from game.utils.constants import SCREEN_WIDTH,SCREEN_HEIGHT,SHIP_SPEED , SPACESHIP,SHIP_WIDTH,SHIP_HEIGHT,X_POS, Y_POS

class Spaceship(Sprite):

    def __init__(self) -> None:
        self.image = SPACESHIP 
        self.image = pygame.transform.scale(self.image,(SHIP_WIDTH,SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = X_POS
        self.rect.x = Y_POS
    
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
        self.rect.x -= SHIP_SPEED
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
            
    def move_right(self):
        self.rect.x += SHIP_SPEED
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0 - SHIP_WIDTH
    
    def move_up(self):
        if self.rect.top != (SCREEN_WIDTH - (SCREEN_WIDTH * 0.90) ):
            self.rect.y -= SHIP_SPEED
    
    def move_down(self):
        if self.rect.y + SHIP_WIDTH != (Y_POS + (Y_POS * 0.10) ):
            self.rect.y += SHIP_SPEED