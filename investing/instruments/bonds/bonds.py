import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from ..instrument import Instrument

class Bond(Instrument):
    def __init__(self, symbol, name, issuer, maturity_date, coupon_rate):
        super().__init__(symbol, name, "Bond")
        self.issuer = issuer
        self.maturity_date = maturity_date
        self.coupon_rate = coupon_rate