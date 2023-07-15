from game.components.enemis.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        if not self.enemies: # len(self.enemies) == 0 # 
            self.enemies.append(Enemy())

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
