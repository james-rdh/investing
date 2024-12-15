from . import Instrument, InstrumentFactory, InstrumentRepository

class Stock(Instrument):
    def __init__(self, ticker, exchange):
        self.ticker = ticker
        self.exchange = exchange

    def get_symbol(self):
        return f"{self.ticker}__{self.exchange}"

class StockFactory(InstrumentFactory):
    def create(self, ticker, exchange):
        stock = Stock(ticker, exchange)
        return stock

class StockRepository(InstrumentRepository):
    def __init__(self):
        self.stocks = [] # storage connection

    def create(self, ticker, exchange):
        instrument = StockFactory.create(ticker, exchange)
        self.stocks.append(instrument)

    def find(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                return stock
        return None

    def update(self, symbol, data):
        for i, stock in enumerate(self.stocks):
            if stock.symbol == data.symbol:
                self.stocks[i] = instrument
                return

    def delete(self, instrument):
        self.stocks.remove(instrument)