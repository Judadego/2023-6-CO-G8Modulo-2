from game.components.power_ups.power_up import PowerUp
from game.utils.constants import DOUBLE,DOUBLE_TYPE

class Double(PowerUp):
    def __init__ (self):
        super().__init__(DOUBLE,DOUBLE_TYPE)