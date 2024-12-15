from ..instruments import Instrument
from ..positions.position import Position

class Portfolio(Instrument):
    def __init__(self, name):
        self.name = name
        self.children = [] # positions

    def get_value(self):
        value = 0
        for position in self.children:
            value += position.calculate_value()
        return value

    def add_position(self, position):
        self.children.append(position)

    def remove_position(self, position):
        self.children.remove(position)