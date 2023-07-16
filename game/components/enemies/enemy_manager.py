import random
import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_IMAGES,ENEMY_COLORS


class EnemyManager():
    
    def __init__(self) -> None:
        self.enemies = []
        self.enemy_images = ENEMY_IMAGES
    
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 1 :
            image = random.choice(ENEMY_IMAGES)
            color = random.choice(ENEMY_COLORS)
            enemy = Enemy(image,color)
            self.enemies.append(enemy)