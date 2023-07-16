import pygame
import os

#pygame.init()
#screen
#screen_info = get_screen_info()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 720 #screen_info.current_h
SCREEN_WIDTH = 1200 #screen_info.current_w
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
#please, add in ENEMY_IMAGES[ENEMY_N]

FONT_STYLE = 'freesansbold.ttf'

#SpaceShip Constants
SHIP_WIDTH = 40
SHIP_HEIGHT = 60
X_POS = (SCREEN_WIDTH // 2 ) - SHIP_WIDTH
Y_POS = 500
SHIP_SPEED = 10

#Enemies Constants
SHIP_WIDTH = 60 
SHIP_HEIGHT = 80 
X_POS_E = [50,100,150,200,250,300,350,400,450,500,550]
Y_POS_E = -20
SPEED_Y = 1 
SPEED_X = 5
MOVE_X = {0:'LEFT',1:'RIGHT'}
ENEMY_IMAGES = [ENEMY_1,ENEMY_2]
ENEMY_COLORS = [
    (255, 0, 0),   # red
    (0, 255, 0),   # green
    (255, 255, 0), # yellow
    (255, 0, 255), # Magenta
    (255, 165, 0), # Orange
    (255,255,255),  # white
    (255,20,147), # deeppink
    (0,255,255)   # cyan
    # add more colors [8 colors X 2 images = 16 Options]
]
