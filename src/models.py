from .database import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

class Date(Base):
    __tablename__ = 'Dates'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)

class Country(Base):
    __tablename__ = 'Countries'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Currency(Base):
    __tablename__ = 'Currencies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Sector(Base):
    __tablename__ = 'Sectors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Industry(Base):
    __tablename__ = 'Industry'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Company(Base):
    __tablename__ = 'Companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Asset(Base):
    __tablename__ = 'Assets'
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, nullable=False)
    name = Column(String, unique=True, nullable=False) 

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Account(Base):
    __tablename__ = 'Accounts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    institution_id = Column(Integer, ForeignKey('AccountInstitutions.id'))
    type_id = Column(Integer, ForeignKey('AccountTypes.id'))
    name = Column(String, nullable=False)
    description = Column(String)
    opened_date = Column(Date, nullable=False)
    closed_date = Column(Date)
    status = Column(String, nullable=False)
    user = relationship("Users", back_populates="Accounts")

class Portfolio(Base):
    __tablename__ = 'Portfolios'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    name = Column(String, nullable=False)
    description = Column(String)
    opened_date = Column(Date, nullable=False)
    closed_date = Column(Date)
    status = Column(String, nullable=False)
    user = relationship("Users", back_populates="Portfolios")

class Position(Base):
    __tablename__ = 'Positions'
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('Assets.id'))
    account_id = Column(Integer, ForeignKey('Accounts.id'))
    portfolio_id = Column(Integer, ForeignKey('Portfolios.id'))
    quantity = Column(Float, nullable=False)
    cost_basis = Column(Float)
    cost_basis_method = Column(String)  # E.g., 'FIFO', 'LIFO'
    asset = relationship("Assets", back_populates="Positions")
    account = relationship("Accounts", back_populates="Positions")
    portfolio = relationship("Portfolios", back_populates="Positions")

class Transaction(Base):
    __tablename__ = 'Transactions'
    id = Column(Integer, primary_key=True)
    # ... other transaction details (type, date, quantity, etc.)
    user_account_id = Column(Integer, ForeignKey('Accounts.id'))
    asset_id = Column(Integer, ForeignKey('Assets.id'))
    fee = Column(Float)
    fee_currency = Column(String)

class Strategy(Base):
    __tablename__ = 'Strategies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship("Users", back_populates="Strategies")

class Indicator(Base):
    __tablename__ = 'Indicators'
    id = Column(Integer, primary_key=True)

class Signal(Base):
    __tablename__ = 'Signals'
    
class Rule(Base):
    __tablename__ = 'Rules'
