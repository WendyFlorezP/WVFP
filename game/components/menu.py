import pygame
from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message):
        self.message = message
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)

    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()

    def reset_screen_color(self, screen):
        screen.fill((225, 225, 225))

    def draw(self, screen, message, X=HALF_SCREEN_WIDTH, Y=HALF_SCREEN_HEIGHT, color=(0, 0, 0), y=None):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        if y is not None:
            text_rect.center = (X, y)
        else:
            text_rect.center = (X, Y)
        screen.fill((225, 225, 255))
        screen.blit(text, text_rect)


    def draw_icon(self, screen):
        screen.blit(self.icon, self.icon_rect)

    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def draw_score(self, message, y_pos, screen):
        message = message
        text = self.font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.HALF_SCREEN_WIDTH, y_pos)
        screen.blit(text, text_rect)



