import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
LIFE =  pygame.image.load(os.path.join(IMG_DIR, "Other/life_spaceship.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'

#SpaceShip Constants
SHIP_WIDTH = 40
SHIP_HEIGHT = 60
X_POS = (SCREEN_WIDTH // 2 ) - SHIP_WIDTH
Y_POS = 500
SHIP_SPEED = 10

#Enemies Constants
SHIP_WIDTH = 40 
SHIP_HEIGHT = 60 
X_POS = [50,100,150,200,250,300,350,400,450,500,550]
Y_POS = 20
SPEED_Y = 1 
SPEED_X = 5
MOVE_X = {0:'LEFT',1:'RIGHT'}
