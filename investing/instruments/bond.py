from . import Instrument, InstrumentFactory, InstrumentRepository

class Bond(Instrument):
    def __init__(self, face_value, coupon_rate, maturity):
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.maturity = maturity
    
    def get_symbol(self):
        return f"{self.face_value}_{self.coupon_rate}_{self.maturity}"

    def get_price(self):
        return self.market_price

class BondFactory(InstrumentFactory):
    def create(self, face_value, coupon_rate, maturity):
        return Bond(face_value, coupon_rate, maturity)