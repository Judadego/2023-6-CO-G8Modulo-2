
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import RAPID_FIRE, RAPID_FIRE_TYPE

class RapidFire(PowerUp):
    def __init__ (self):
        super().__init__(RAPID_FIRE,RAPID_FIRE_TYPE)