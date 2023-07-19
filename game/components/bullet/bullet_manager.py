from game.utils.constants import SCORE
import pygame 
from pygame.sprite import Group

class BulletManager:
    def __init__(self):
        self.enemy_bullets = Group()
        self.player_bullets = Group()
        self.count_bullet = 0
        self.last_player_bullet_time = 0
        self.player_bullet_delay = 300
        self.last_enemy_bullet_time = 0
        self.enemy_bullet_delay = 600

    def update(self, game):
    
            for bullet in self.enemy_bullets:
                bullet.update(self.enemy_bullets)
                if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                    bullet.kill()
                    game.player.is_dead = True
                    game.death_score += 1 
                    pygame.time.delay(1000)
                    break
    
            for bullet in self.player_bullets:
                bullet.update(self.player_bullets)
                for enemy in game.enemy_manager.enemies:
                    if bullet.rect.colliderect(enemy) and bullet.owner == 'player':                        
                        enemy.kill()
                        bullet.kill()    
                        game.update_score(SCORE) 
                        print(game.score)       

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

    def add_bullet(self, bullet):
        """agrega bullet, enemigos como del player

        Args:
            bullet (_type_): _description_
        """
        if bullet.owner == 'enemy':
            num_bullet = 1000
            current_time = pygame.time.get_ticks()
            if len(self.enemy_bullets) < num_bullet and current_time - self.last_enemy_bullet_time > self.enemy_bullet_delay:                
                self.enemy_bullets.add(bullet)
                self.count_bullet += num_bullet
                self.last_enemy_bullet_time = current_time
        elif bullet.owner == 'player':
            current_time = pygame.time.get_ticks()
            if current_time - self.last_player_bullet_time > self.player_bullet_delay:
                self.player_bullets.add(bullet)
                self.last_player_bullet_time = current_time