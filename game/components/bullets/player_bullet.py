import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET_PLAYER, PLAYER_TYPE



class Player_Bullet(Sprite):
    SPEED = 20
    BULLETS = { PLAYER_TYPE: BULLET_PLAYER }

    def __init__(self, spaceship):
        self.ower = spaceship.type 
        self.image = pygame.transform.scale(self.BULLETS[spaceship.type], (10, 30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets):
        if self.ower == PLAYER_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)