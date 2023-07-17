from game.components.enemis.enemy import Enemy
from game.components.enemis.enemy2 import Enemy2


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy2_spawned = False

    def update(self):
        if not self.enemies:
            self.enemies.append(Enemy())
        elif not self.enemy2_spawned:
            last_enemy = self.enemies[-1]
            if isinstance(last_enemy, Enemy):
                self.enemies.append(Enemy2())
                self.enemy2_spawned = True
    
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)