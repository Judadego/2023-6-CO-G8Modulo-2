import random
import pygame

from game.components.power_ups.rapid_fire import RapidFire
from game.components.power_ups.shield import Shield

from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE,POWER_UP_SOUND
from game.utils.constants import POWER_UP_DURATION, RAPID_FIRE_TYPE, SPACESHIP

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)
        self.power_up_sound = POWER_UP_SOUND

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len (self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            print("1---------------")
            print(game.player.has_power_up)
            print(game.player.power_time_up)
            print(power_up.start_time)
            
            if game.player.rect.colliderect(power_up):
                pygame.mixer.Sound(self.power_up_sound)
                if game.player.power_up_type != SHIELD_TYPE or game.player.power_up_type != RAPID_FIRE_TYPE  and not game.player.is_dead:                    
                    power_up.start_time = pygame.time.get_ticks()                    
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True 
                    game.player.power_time_up = (power_up.start_time /2 ) * POWER_UP_DURATION    #(self.duration * 100 )  # power_up.start_time
                    #game.player.power_time_up = power_up.start_time + random.randint(3000, 5000)  # Duración de 3 a 5 segundos
                    if game.player.power_up_type == SHIELD_TYPE:
                        game.player.set_image((65, 75), SPACESHIP_SHIELD)
                        self.power_ups.remove(power_up)
                    elif game.player.power_up_type == RAPID_FIRE_TYPE:                        
                        game.player.set_image((65, 75), SPACESHIP)
                        self.power_ups.remove(power_up)
                else:
                    self.power_ups.remove(power_up)
                print("2---------------")
                print(game.player.has_power_up)
                print(game.player.power_time_up)
                print(power_up.start_time)

    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up_type = random.choice([Shield,RapidFire])
        power_up = power_up_type()       
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)
        #pygame.time.set_timer(POWER_UP_TIMER_EVENT, POWER_UP_DURATION)  # Configura el temporizador