from ..instruments import Instrument

class Position(Instrument):
    def __init__(self, instrument, quantity):
        self.instrument = instrument
        self.quantity = quantity

    def calculate_value(self):
        return self.instrument.calculate_value() * self.quantity