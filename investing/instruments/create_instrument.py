from .instrument import Instrument

class InstrumentFactory:
    def create_instrument(id, type, symbol, name):
        return Instrument(id, type, symbol, name)

