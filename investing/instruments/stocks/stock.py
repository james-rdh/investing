import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from ..instrument import Instrument

class Stock(Instrument):
    def __init__(self, symbol, name, exchange):
        super().__init__(symbol, name, "Stock")
        self.exchange = exchange