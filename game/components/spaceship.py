import pygame
from pygame.sprite import Sprite 

from game.utils.constants import DEFAULT_TYPE, PLAYER_TYPE, SCREEN_HEIGHT, SPACESHIP, SCREEN_WIDTH
from game.utils.constants import SPACESHIP_WIDTH, SPACESHIP_HEIGHT



class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30
    Y_POS = 500
    SPACESHIP_WIDTH = 60
    SPACESHIP_HEIGHT = 60
    def __init__(self):
         self.type = PLAYER_TYPE
         self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
         self.rect = self.image.get_rect()
         self.rect.x = self.X_POS
         self.rect.y = self.Y_POS
         self.power_up_type = DEFAULT_TYPE
         self.power_up_time = 0

    def update(self, user_input, bullet_manager):

        self.moving_left = bool(user_input[pygame.K_LEFT])

        self.moving_right = bool(user_input[pygame.K_RIGHT])
        
        self.moving_up = bool(user_input[pygame.K_UP])

        self.moving_down = bool(user_input[pygame.K_DOWN])
        
        self.move()
        if (user_input[pygame.K_k]):
            self.shoot(bullet_manager)

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
        if self.rect.left < 0:
            screen.blit(self.image, (SCREEN_WIDTH + self.rect.x, self.rect.y))
        if self.rect.right > SCREEN_WIDTH:
            screen.blit(self.image, (self.rect.x - SCREEN_WIDTH, self.rect.y))
            self.player.draw_power_up(self.screen, self.menu)
            
    def shoot(self, bullet_manager):
        bullet_manager.add_bullet(self)

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def on_pick_power_up(self, time_up, type, image):
        self.image = pygame.transform.scale(image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.power_up_time_up = time_up
        self.power_up_type = type

    def draw_power_up(self, game, font):
        if self.power_up_type != DEFAULT_TYPE:
            time_left = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_left >= 0:
                text_surface = font.render(f"{self.power_up_type.capitalize()} is enabled for {time_left} seconds", True, (225, 225, 225))
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
                game.screen.blit(text_surface, text_rect)
            else:
                self.power_up_type = DEFAULT_TYPE
                self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))



