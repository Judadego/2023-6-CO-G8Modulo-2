import random
import pygame
from pygame.sprite import Group

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_IMAGES,ENEMY_COLORS , SHIELD_TYPE, SCORE,KILL_ENEMY_SOUND
from game.utils.constants import ENEMY_1,ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH,MOVE_X,DOUBLE_TYPE
from game.utils.constants import SHIP_WIDTH,SHIP_HEIGHT,X_POS_E,Y_POS_E,SPEED_Y , SPEED_X


class EnemyManager():
    
    def __init__(self) -> None:
        self.enemies = Group()
        #self.enemies = []
        self.enemy_images = ENEMY_IMAGES        
        self.kill_enemy_sound = KILL_ENEMY_SOUND
        self.enemy_dead = 0
    
    def update(self, game):
        self.add_enemy(game)            
        #lógica para que cuando la nave enemiga choque con player, perdemos la vida
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            if enemy.rect.colliderect(game.player.rect) and not game.player.is_dead:
                
                    if game.player.power_up_type != SHIELD_TYPE :
                        if game.player.extra_life == 0:
                            game.player.is_dead = True
                            game.death_score += 1   
                            pygame.time.delay(500)
                            break
                        else: 
                            game.player.extra_life -= 1
                            enemy.kill()
                            pygame.mixer.Sound.play(self.kill_enemy_sound)  
                    else:
                        enemy.kill()
                        pygame.mixer.Sound.play(self.kill_enemy_sound)
                        if (game.power_up_manager.double_active):
                            game.update_score(SCORE) 
                        game.update_score(SCORE)
                        self.enemy_dead += 1

  
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self, game):
        min = 1
        max = 3
        if game.power_up_manager.double_active:
            min = min * 2 
            max = max * 2
        num_enemy = random.randint(min,max)
        
        if len(self.enemies) < num_enemy :
            image = random.choice(ENEMY_IMAGES)
            color = random.choice(ENEMY_COLORS)
            speed_y = random.choice(SPEED_Y)
            speed_x = random.choice(SPEED_X)
            move_x_for = (30,100)
            enemy = Enemy(image,color,speed_x,speed_y,move_x_for)
            #self.enemies.append(enemy)
            self.enemies.add(enemy)

            