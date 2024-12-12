import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from ..instrument import Instrument

class Cash(Instrument):
    def __init__(self, symbol, name, currency):
        super().__init__(symbol, name, "Cash")
        self.currency = currency