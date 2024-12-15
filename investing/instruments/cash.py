from . import Instrument, InstrumentFactory

class Cash(Instrument):
    def __init__(self, currency, amount):
        self.currency = currency

    def get_symbol(self):
        return f"{self.currency}"

class CashFactory(InstrumentFactory):
    def create(self, currency, amount):
        return Cash(currency, amount)