import random
import pygame

from game.components.power_ups.rapid_fire import RapidFire
from game.components.power_ups.shield import Shield
from game.components.power_ups.extra_life import ExtraLife
from game.components.power_ups.double import Double
from pygame.sprite import Group

from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE,POWER_UP_SOUND,SHIP_WIDTH, SHIP_HEIGHT, DOUBLE
from game.utils.constants import POWER_UP_DURATION, RAPID_FIRE_TYPE, SPACESHIP, EXTRA_LIFE_TYPE,DOUBLE_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)
        self.power_up_sound = POWER_UP_SOUND
        self.double_active = False

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len (self.power_ups) == 0 and current_time >= self.when_appears :
            self.generate_power_up(game)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            if game.player.rect.colliderect(power_up) and not game.player.is_dead:
                pygame.mixer.Sound.play(self.power_up_sound)
                if power_up.type != EXTRA_LIFE_TYPE and power_up.type != DOUBLE_TYPE:
                    
                    if game.player.power_up_type != SHIELD_TYPE or game.player.power_up_type != RAPID_FIRE_TYPE  and not game.player.is_dead :                    
                        power_up.start_time = pygame.time.get_ticks()                    
                        game.player.power_up_type = power_up.type
                        game.player.has_power_up = True 
                        game.player.power_time_up = power_up.start_time + (self.duration * 1000 ) #random.randint(3000, 5000)  # Duración de 3 a 5 segundos
                        
                        if game.player.power_up_type == SHIELD_TYPE:
                            game.player.set_image(( SHIP_WIDTH*1.5,SHIP_HEIGHT), SPACESHIP_SHIELD) ##
                            #self.power_ups.remove(power_up)
                            
                        elif game.player.power_up_type == RAPID_FIRE_TYPE:                        
                            game.player.set_image((SHIP_WIDTH,SHIP_HEIGHT), SPACESHIP)
                            #self.power_ups.remove(power_up)     
                        #self.power_ups.remove(power_up)
                            
                elif power_up.type == EXTRA_LIFE_TYPE and not game.player.is_dead and game.player.extra_life < 10:
                    game.player.extra_life += 1   
                    #self.power_ups.remove(power_up)
                
                elif power_up.type == DOUBLE_TYPE and not self.double_active :
                    self.double_active = True                        
                    power_up.start_time = pygame.time.get_ticks()                    
                    game.player.power_up_type = power_up.type
                    #game.player.has_power_up = True 
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000 )
                    
                self.power_ups.remove(power_up)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self, game):
        max = 10000
        min = 5000
        power_up_type = random.choice([Shield,RapidFire,ExtraLife, Double])
        power_up = power_up_type()    
        if game.power_up_manager.double_active: 
            max = max / 3
            min = min / 3
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)