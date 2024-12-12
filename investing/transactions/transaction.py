from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    type = Column(String)
    instrument_id = Column(Integer, ForeignKey('intruments.id'))
    price = Column(Integer)
    datetime = Column(DateTime)