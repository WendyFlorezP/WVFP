from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE


class shield(PowerUp):
 def __init__(self):
  super().__init__(SHIELD, SHIELD_TYPE, SPACESHIP_S)
  self.spaceship_image =