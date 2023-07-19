from game.components.menu import Menu
import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemis.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.spaceship import Spaceship
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.max_score = 0
        self.current_score = 0
        self.death_count = 0
        self.highest_score = 0
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        bullet_manager = BulletManager()  
        self.player = Spaceship(bullet_manager)


        self.menu = Menu("Press any key to start...")
        self.score = 0
        self.death_count 
        
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.display.quit()
        pygame.quit()
       
    def play(self):
        self.playing = True
        self.enemy_manager.reset()
        self.score = 0
        self.max_score = self.highest_score
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.draw_game_info()

    def reset_game_info(self):
        self.death_count = 0
        self.max_score = self.highest_score

    def show_menu(self):
         if self.death_count > 0:
            self.menu.update_message(f"You died. Press any key to start again.../(.,-,.)/{self.death_count}")
            self.menu.update_message(f"Your score is : {self.score}")
         if self.score > self.max_score:
             self.max_score = 0
             self.max_score += self.score
             self.menu.update_message(f"your highest score is: {self.max_score}")
         else:
            self.menu.update_message("Press any key to start...┐(.-.)┌")
         self.menu.draw(self.screen)
         self.menu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False
        self.player_death(self.score)
        self.draw_game_info()
        pygame.display.update()
        pygame.time.delay(2000)
        print("Current Score:", self.score)
        print("Deaths:", self.death_count)
        print("Highest Score Achieved:", self.max_score)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_close()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input ,self.bullet_manager) 
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw_game_info(self):
        font = pygame.font.Font(FONT_STYLE, 18)

        current_score_surface = font.render(f"Current Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(current_score_surface, (10, SCREEN_HEIGHT - 60))

        deaths_surface = font.render(f"Deaths: {self.death_count}", True, (255, 255, 255))
        self.screen.blit(deaths_surface, (10, SCREEN_HEIGHT - 40))

        highest_score_surface = font.render(f"Highest Score Achieved: {self.max_score}", True, (255, 255, 255))
        self.screen.blit(highest_score_surface, (10, SCREEN_HEIGHT - 20))


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) 
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.draw_game_info()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):

        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed 

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def player_death(self, score):
        if score > self.highest_score:
            self.highest_score = score
            self.death_count += 1
        
