import pygame


class PlayerBulletManager:
    def __init__(self):
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.bullets.update()

    def draw(self, screen):
        self.bullets.draw(screen)

    def add_bullet(self, bullet):
        self.bullets.add(bullet)