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

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/espacio_2.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

YOU_WIN =pygame.image.load(os.path.join(IMG_DIR, "Other/YOUWIN.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
ENEMY_TYPE = "enemy"
PLAYER_TYPE = "player"
SPACESHIP_WIDTH = 60
SPACESHIP_HEIGHT = 60
HEART_TYPE = "heart"


SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_5.png"))


BULLET_PLAYER = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_5.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_7.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_8.png"))


FONT_STYLE = "game/assets/Other/04B_30__.TTF"