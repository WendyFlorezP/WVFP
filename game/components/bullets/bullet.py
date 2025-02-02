import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT



class Bullet(Sprite):
    SPEED = 20
    BULLETS = { ENEMY_TYPE: BULLET_ENEMY }

    def __init__(self, spaceship):
        self.ower = spaceship.type 
        self.image = pygame.transform.scale(self.BULLETS[spaceship.type], (10, 30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets):
        if self.ower == ENEMY_TYPE:
            self.rect.y += self.SPEED
        else:
            self.rect.y += self.SPEED

        if self.rect.y >= SCREEN_HEIGHT: 
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
