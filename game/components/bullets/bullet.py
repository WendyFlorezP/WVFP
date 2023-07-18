import pygame
from pygame.sprite import Sprite
from game.components.spaceship import Spaceship
from game.utils.constants import BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):
    SPEED = 20
    BULLETS = { ENEMY_TYPE: BULLET_ENEMY }

    def __init__(self, spaceship, x, y):
        super().__init__()
        self.ower = spaceship.type 
        self.owner = spaceship
        self.image = pygame.transform.scale(self.BULLETS[spaceship.type], (10, 30))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x, y, 5, 10)
        self.rect.center = spaceship.rect.center

    def update(self, bullets):
        self.rect.y -= Spaceship.BULLET_SPEED
        if self.rect.y <= 0:
            bullets.remove(self)
        if self.ower == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

