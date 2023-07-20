import pygame
from game.utils.constants import FONT_STYLE


class Counter:
    def __init__(self, name):
     self.count = 0
     self.name = name

    def update(self, new_count = None):
       if new_count:
        self.count = new_count
       else:
        self.count += 1 

    def draw(self, screen, color=(255, 255, 255), center_position=(10000, 15000)):
     font = pygame.font.Font(FONT_STYLE, 30)
     text = font.render(f'{self.name}: {self.count}', True, color)
     text_rect = text.get_rect()
     text_rect.center = center_position
     screen.blit(text, text_rect)

    def reset(self):
     self.count = 0 