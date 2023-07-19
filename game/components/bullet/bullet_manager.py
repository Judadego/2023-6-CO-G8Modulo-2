import pygame 
from pygame.sprite import Group

class BulletManager:
    def __init__(self):
        self.enemy_bullets = Group()
        self.player_bullets = Group()
        self.count_bullet = 0

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
                        game.score += 100         

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
        num_bullet = 5

        if bullet.owner == 'enemy' and len (self.enemy_bullets) < num_bullet:
            self.enemy_bullets.add(bullet)
            self.count_bullet += num_bullet
        else:
            self.player_bullets.add(bullet)