import pygame
from pygame.sprite import Sprite 

from game.utils.constants import SCREEN_HEIGHT, SPACESHIP, SCREEN_WIDTH


class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30
    Y_POS = 500
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.bullet_manager = None

    def update(self, user_input):
        if user_input[pygame.K_k]:
            bullet_x = self.rect.centerx
            bullet_y = self.rect.top
            self.bullet_manager.add_bullet(self, bullet_x, bullet_y)

        self.moving_left = bool(user_input[pygame.K_LEFT])

        self.moving_right = bool(user_input[pygame.K_RIGHT])
        
        self.moving_up = bool(user_input[pygame.K_UP])

        self.moving_down = bool(user_input[pygame.K_DOWN])
        
        self.move()
        
    def set_bullet_manager(self, bullet_manager):
        self.bullet_manager = bullet_manager

    def move(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 10
        elif self.moving_right and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        elif self.moving_right and self.rect.right >= SCREEN_WIDTH:
            self.rect.x = 0
        elif self.moving_left and self.rect.left <= 0:
            self.rect.x = SCREEN_WIDTH - self.rect.width
            
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 10
        elif self.moving_down and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
   