class Instrument:
    def __init__(self, symbol, name=None):
        self.symbol = symbol
        self.name = name

    def __str__(self):
        return f"{self.symbol} - {self.name}"

### usage
# example = Instrument(":)", "Example Instrument")
# print(example)
### expected output
# :) - Example Instrument

class InstrumentFactory:
    def create_instrument(type, symbol, name):
        return Instrument(id, type, symbol, name)

class Bond(Instrument):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.instrument_type = super().__getattribute__("__name__")
    
    def __str__(self):
        return f"{super().__init__(self.symbol, self.name)} ({self.instrument_type})"

example = Bond(":)", "Example Bond")
print(example)

class Cash(Instrument):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        # self.currency = currency