from . import Instrument#, InstrumentRepository, InstrumentComparer, InstrumentAnalyser

class ETF(Instrument):
    def __init__(self, ticker, exchange):
        self.ticker = ticker
        self.exchange = exchange
        self.market_price = None

    def get_symbol(self):
        return f"{self.ticker}_{self.exchange}"

    def get_price(self):
        return self.market_price