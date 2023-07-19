from game.components.enemis.enemy import Enemy
from game.components.enemis.enemy2 import Enemy2
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy2_spawned = False

    def update(self, game):
        if not self.enemies:
                choose_ship = random.choice([Enemy2, Enemy])
                self.enemies.append(choose_ship())
    
        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def reset(self):
         self.enemies = []