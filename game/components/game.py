from game.components.menu import Menu
import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemis.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.spaceship import Spaceship
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from game.components.power_ups.power_up_manager import PowerUpManager

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
        self.power_up_manager = PowerUpManager()
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
         half_screen_width = SCREEN_WIDTH // 2
         if self.death_count > 0:
            self.menu.reset_screen_color(self.screen)
            self.menu.draw(self.screen, "Press any key to start...┐(.-.)┌")
         else:
            self.menu.reset_screen_color(self.screen)
            self.menu.draw(self.screen, "You died. Press any key to start again.../(.,-,.)/")
            font = pygame.font.Font(FONT_STYLE, 18)
            score_text = font.render(f"Your score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (half_screen_width, 350))
            highest_score_text = font.render(f"Highest score: {self.highest_score}", True, (255, 255, 255))
            self.screen.blit(highest_score_text, (half_screen_width, 400))
            death_count_text = font.render(f"Total deaths: {self.death_count}", True, (255, 255, 255))
            self.screen.blit(death_count_text, (half_screen_width, 450))
            self.menu.draw(self.screen)
            self.menu.events(self.on_close, self.play)
            pygame.display.flip()
            
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.update(self.score.count)
        

    
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
        self.power_up_manager.update(self)

    def draw_game_info(self):
        font = pygame.font.Font(FONT_STYLE, 18)

        current_score_surface = font.render(f"Current Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(current_score_surface, (10, SCREEN_HEIGHT - 60))

        deaths_surface = font.render(f"Deaths: {self.death_count}", True, (255, 255, 255))
        self.screen.blit(deaths_surface, (10, SCREEN_HEIGHT - 40))

        highest_score_surface = font.render(f"Highest Score Achieved: {self.max_score}", True, (255, 255, 255))
        self.screen.blit(highest_score_surface, (10, SCREEN_HEIGHT - 20))

        result_surface = font.render(f"Score: {self.score}  Deaths: {self.death_count}  Highest Score: {self.max_score}", True, (255, 255, 255))
        self.screen.blit(result_surface, (10, SCREEN_HEIGHT - 80))



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) 
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
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

    def player_death(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.death_count += 1

    def reset(self):
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.power_up_manager.reset()
        self.score.reset()
        self.player.reset()        

