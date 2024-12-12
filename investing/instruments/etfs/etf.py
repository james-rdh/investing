import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from ..instrument import Instrument

class ETF(Instrument):
    def __init__(self, symbol, name, index):
        super().__init__(symbol, name, "ETF")
        self.index = index

# class MutualFund(Instrument):
#     def __init__(self, symbol, name, fund_manager):
#         super().__init__(symbol, name, "Mutual Fund")
#         self.fund_manager = fund_manager