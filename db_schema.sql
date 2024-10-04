CREATE TABLE IF NOT EXISTS Instruments (
    id INTEGER PRIMARY KEY,
    symbol TEXT UNIQUE NOT NULL,
    type TEXT DEFAULT 'STOCK',
    name TEXT,
    sector TEXT
);
CREATE TABLE IF NOT EXISTS Positions (
    id INTEGER PRIMARY KEY,
    instrument_id INTEGER REFERENCES Instruments(id),
    type TEXT DEFAULT 'LONG',
    quantity REAL NOT NULL DEFAULT 1,
    average_purchase_price REAL,
    total_cost_basis REAL,
    market_value REAL
);
CREATE TABLE IF NOT EXISTS Portfolios (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    type TEXT,
    created_date TEXT DEFAULT CURRENT_DATE,
    updated_date TEXT DEFAULT CURRENT_DATE,
    risk_tolerance TEXT,
    currency TEXT DEFAULT 'USD',
    cash_balance REAL DEFAULT 0,
    total_market_value REAL
);
CREATE TABLE IF NOT EXISTS Transactions (
    id INTEGER PRIMARY KEY,
    position_id INTEGER REFERENCES Positions(id),
    date TEXT NOT NULL,
    purchase_price REAL,
    transaction_cost REAL
);
CREATE TABLE IF NOT EXISTS PortfolioPositions (
    id INTEGER PRIMARY KEY,
    portfolio_id INTEGER REFERENCES Portfolios(id),
    position_id INTEGER REFERENCES Positions(id),
    UNIQUE(portfolio_id, position_id)
);
CREATE TABLE IF NOT EXISTS InstrumentOHLCVs (
    id INTEGER PRIMARY KEY,
    instrument_id INTEGER REFERENCES Instruments(id),
    date TEXT NOT NULL,
    open REAL NOT NULL,
    high REAL NOT NULL,
    low REAL NOT NULL,
    close REAL NOT NULL,
    volume INTEGER NOT NULL,
    UNIQUE(instrument_id, date)
);
CREATE TABLE IF NOT EXISTS PositionTransactions (
    id INTEGER PRIMARY KEY,
    position_id INTEGER REFERENCES Positions(id),
    transaction_id INTEGER REGERENCE Transactions(id),
    UNIQUE(position_id, transaction_id)
);