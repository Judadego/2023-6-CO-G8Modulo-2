import random
import pygame
from pygame.sprite import Group

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_IMAGES,ENEMY_COLORS
from game.utils.constants import ENEMY_1,ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH,MOVE_X
from game.utils.constants import SHIP_WIDTH,SHIP_HEIGHT,X_POS_E,Y_POS_E,SPEED_Y , SPEED_X


class EnemyManager():
    
    def __init__(self) -> None:
        self.enemies = Group()
        #self.enemies = []
        self.enemy_images = ENEMY_IMAGES
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        
        num_enemy = random.randint(1,3)
        if len(self.enemies) < num_enemy :
            image = random.choice(ENEMY_IMAGES)
            color = random.choice(ENEMY_COLORS)
            speed_y = random.choice(SPEED_Y)
            speed_x = random.choice(SPEED_X)
            move_x_for = (30,100)
            enemy = Enemy(image,color,speed_x,speed_y,move_x_for)
            #self.enemies.append(enemy)
            self.enemies.add(enemy)

            