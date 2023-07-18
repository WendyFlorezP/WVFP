import pygame
from game.components import spaceship
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE


class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.bullets = []

    def update(self, game):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
            for bullet in self.bullets:
                bullet.update(self.bullets)

    def draw(self,screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self,x, y):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))
            new_bullet = Bullet(spaceship, x, y)
            self.bullets.append(new_bullet)

    
    