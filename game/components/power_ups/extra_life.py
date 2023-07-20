from game.components.power_ups.power_up import PowerUp
from game.utils.constants import EXTRA_LIFE, EXTRA_LIFE_TYPE

class ExtraLife(PowerUp):
    def __init__ (self):
        super().__init__(EXTRA_LIFE, EXTRA_LIFE_TYPE)