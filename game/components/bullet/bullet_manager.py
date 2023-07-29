import pygame 

from game.utils.constants import SCORE, PLAYER_SOUND, RAPID_FIRE_TYPE
from game.utils.constants import SHIELD_TYPE, KILL_ENEMY_SOUND, DOUBLE_TYPE

from pygame.sprite import Group

class BulletManager:
    PLAYER_DELAY = 250
    def __init__(self):
        self.enemy_bullets = Group()
        self.player_bullets = Group()
        self.count_bullet = 0
        self.last_player_bullet_time = 0
        self.player_bullet_delay = self.PLAYER_DELAY
        self.last_enemy_bullet_time = 0
        self.enemy_bullet_delay = 600        
        self.player_shoot_sound = PLAYER_SOUND
        self.kill_enemy_sound = KILL_ENEMY_SOUND

    def update(self, game):
    
            for bullet in self.enemy_bullets:
                bullet.update(self.enemy_bullets)
                if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':

                        if game.player.power_up_type != SHIELD_TYPE and not game.player.is_dead:
                            #game.playing = False
                            if game.player.extra_life == 0:
                                pygame.time.delay(1000)
                                game.player.is_dead = True
                                game.death_score += 1 
                                
                                break
                            else:
                                game.player.extra_life -= 1
                        bullet.kill()
    
            for bullet in self.player_bullets:
                bullet.update(self.player_bullets)
                for enemy in game.enemy_manager.enemies:
                    if bullet.rect.colliderect(enemy) and bullet.owner == 'player' and not game.player.is_dead:                        
                        enemy.kill()
                        pygame.mixer.Sound.play(self.kill_enemy_sound) 
                        bullet.kill()    
                        game.enemy_manager.enemy_dead += 1
                        if game.power_up_manager.double_active:
                            game.update_score(SCORE)
                        game.update_score(SCORE)  


    def draw(self, screen,enemy_manager):
        """ Agregamos validacion dentro del for ya que 
            no renderizaba correctamente las balas enemigas
        """        
        for bullet in self.enemy_bullets:
            if bullet.owner == 'enemy':
                   bullet.draw(screen)

        for bullet in self.player_bullets:
            if bullet.owner == 'player':
                    bullet.draw(screen)

    def add_bullet(self, bullet, game):
        """agrega bullet, enemigos como del player

        Args:
            bullet (_type_): _description_
        """
        if bullet.owner == 'enemy' :
            num_bullet = 1000
            if game.power_up_manager.double_active:
                num_bullet = 1000 * 3
            current_time = pygame.time.get_ticks()
            if len(self.enemy_bullets) < num_bullet and current_time - self.last_enemy_bullet_time > self.enemy_bullet_delay:                
                self.enemy_bullets.add(bullet)
                self.count_bullet += num_bullet
                self.last_enemy_bullet_time = current_time
        elif bullet.owner == 'player':
            current_time = pygame.time.get_ticks()
            if game.player.has_power_up and game.player.power_up_type == RAPID_FIRE_TYPE:
                self.player_bullet_delay = self.PLAYER_DELAY / 2
            else:
                 self.player_bullet_delay = self.PLAYER_DELAY
            if current_time - self.last_player_bullet_time > self.player_bullet_delay:
                self.player_bullets.add(bullet)
                pygame.mixer.Sound.play(self.player_shoot_sound)  
                self.last_player_bullet_time = current_time