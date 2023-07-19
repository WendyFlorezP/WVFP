import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE
from game.components.bullets.player_bullet import Player_Bullet

class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.Player_Bullet = []

    
    def update(self, game):
     for bullet in self.Player_Bullet:
         bullet.update(self.Player_Bullet)
         for enemy in game.enemy_manager.enemies:
            if bullet.rect.colliderect(enemy.rect):
                game.enemy_manager.enemies.remove(enemy)
                self.Player_Bullet.remove(bullet)
                game.score += 1

     for enemy_bullet in self.enemy_bullets:
         enemy_bullet.update(self.enemy_bullets)
         if enemy_bullet.rect.colliderect(game.player.rect):
            self.enemy_bullets.remove(enemy_bullet)
            game.playing = False
            game.death_count += 1
            print(game.death_count)
            pygame.time.delay(1000)
            break

         for player_bullet in self.Player_Bullet:
             player_bullet.update(self.Player_Bullet)
            


    def draw(self,screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)
        for player_bullet in self.Player_Bullet:
            player_bullet.draw(screen)

    def add_bullet(self, spaceship):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))
        elif spaceship.type == PLAYER_TYPE:
            self.Player_Bullet.append(Player_Bullet(spaceship))

    def reset(self):
        self.enemies = []

