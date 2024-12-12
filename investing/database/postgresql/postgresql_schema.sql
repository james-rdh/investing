CREATE TABLE Dates (
    date DATE PRIMARY KEY,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    week INTEGER,
    day_of_week INTEGER,
    day_of_month INTEGER,
    day_of_quarter INTEGER,
    day_of_year INTEGER
);

CREATE TABLE Countries (
    id SERIAL PRIMARY KEY,
    iso_3166_1_alpha_2_code INTEGER,
    name TEXT NOT NULL UNIQUE,
    continent TEXT,
    region TEXT,
    subregion TEXT,
    capital TEXT,
    location TEXT,
    area TEXT,
    population INTEGER,
    gdp INTEGER,
    gini REAL,
    hdi REAL,
    currency_id INTEGER,
    timezone TEXT,
    internet_tld TEXT
);

CREATE TABLE Currencies (
    code TEXT PRIMARY KEY, -- iso 4127
    name TEXT NOT NULL UNIQUE,
    unit TEXT,
    symbol TEXT
);

CREATE TABLE Sectors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
); -- gics
CREATE TABLE Industries (
    id SERIAL PRIMARY KEY,
    sector_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    FOREIGN KEY (sector_id) REFERENCES Sectors(id)
); -- gics

CREATE TABLE Companies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    country_id INTEGER NOT NULL,
    sector_id INTEGER NOT NULL,
    industry_id INTEGER NOT NULL,
    website_url TEXT,
    address TEXT,
    cik INTEGER,
    FOREIGN KEY (sector_id) REFERENCES Sectors(id),
    FOREIGN KEY (industry_id) REFERENCES Industries(id),
    FOREIGN KEY (country_id) REFERENCES Countries(id)
);

CREATE TABLE MarketTypes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);
CREATE TABLE Markets (
    id SERIAL PRIMARY KEY,
    type_id INTEGER NOT NULL,
    country_id INTEGER,
    local_open TEXT,
    local_close TEXT,
    notes TEXT,
    FOREIGN KEY (type_id) REFERENCES MarketTypes(id),
    FOREIGN KEY (country_id) REFERENCES Countries(id)
);
CREATE TABLE Exchanges (
    id SERIAL PRIMARY KEY,
    market_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (market_id) REFERENCES Markets(id)
);

CREATE TABLE AssetClasses (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
); -- stocks, bonds, cash, commodities, real estate, cryptocurrencies
CREATE TABLE AssetTypes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
); -- cash, derivative

CREATE TABLE InstrumentTypes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    asset_class_id INTEGER NOT NULL,
    asset_type_id INTEGER NOT NULL,
    FOREIGN KEY (asset_class_id) REFERENCES AssetClasses(id),
    FOREIGN KEY (asset_type_id) REFERENCES AssetTypes(id)
); -- stocks, bonds, ETFs, cash, etc.

CREATE TABLE StockTypes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE Stocks (
    id SERIAL PRIMARY KEY,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    symbol TEXT NOT NULL,
    exchange_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    ipo_date DATE,
    FOREIGN KEY (type_id) REFERENCES StockTypes(id),
    FOREIGN KEY (exchange_id) REFERENCES Exchanges(id),
    FOREIGN KEY (currency_id) REFERENCES Currencies(id),
    FOREIGN KEY (company_id) REFERENCES Companies(id),
    FOREIGN KEY (ipo_date) REFERENCES Dates(date),
    UNIQUE(symbol, exchange_id)
);

CREATE TABLE ETFs (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    symbol TEXT NOT NULL,
    exchange_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    issuer_id INTEGER,
    inception_date DATE,
    expense_ratio REAL,
    aum REAL,
    category TEXT,
    focus TEXT,
    dividend_yield REAL,
    FOREIGN KEY (exchange_id) REFERENCES Exchanges(id),
    FOREIGN KEY (currency_id) REFERENCES Currencies(id),
    FOREIGN KEY (issuer_id) REFERENCES Companies(id),
    FOREIGN KEY (inception_date) REFERENCES Dates(date),
    UNIQUE(symbol, exchange_id)
);

CREATE TABLE Bonds (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    symbol TEXT NOT NULL,
    exchange_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    issuer_id INTEGER,
    maturity_date DATE,
    coupon_rate REAL,
    FOREIGN KEY (exchange_id) REFERENCES Exchanges(id),
    FOREIGN KEY (currency_id) REFERENCES Currencies(id),
    FOREIGN KEY (issuer_id) REFERENCES Companies(id),
    FOREIGN KEY (maturity_date) REFERENCES Dates(date),
    UNIQUE(symbol, exchange_id)
);

CREATE TABLE Cash (
    id SERIAL PRIMARY KEY,
    country_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES Countries(id),
    FOREIGN KEY (currency_id) REFERENCES Currencies(id),
    UNIQUE(country_id, currency_id)
);

CREATE TABLE CashAccounts (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    company_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    FOREIGN KEY (company_id) REFERENCES Companies(id),
    FOREIGN KEY (currency_id) REFERENCES Currencies(id),
    UNIQUE(company_id, currency_id)
);

CREATE TABLE BankAccountTypes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE BankAccounts (
    id SERIAL PRIMARY KEY,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    company_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    FOREIGN KEY (type_id) REFERENCES BankAccountTypes(id),
    FOREIGN KEY (company_id) REFERENCES Companies(id),
    FOREIGN KEY (currency_id) REFERENCES Currencies(id)
);

CREATE TABLE OptionTypes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE Options (
    id SERIAL PRIMARY KEY,
    type_id INTEGER NOT NULL,
    underlying_asset_id INTEGER NOT NULL,
    expiry_date DATE NOT NULL,
    strike_price REAL NOT NULL,
    FOREIGN KEY (type_id) REFERENCES OptionTypes(id),
    FOREIGN KEY (underlying_asset_id) REFERENCES Assets(id),
    FOREIGN KEY (expiry_date) REFERENCES Dates(date),
    UNIQUE(type_id, underlying_asset_id, expiry_date, strike_price)
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_date DATE NOT NULL,
    removed_date DATE,
    status TEXT,
    FOREIGN KEY (created_date) REFERENCES Dates(date),
    FOREIGN KEY (removed_date) REFERENCES Dates(date)
);

CREATE TABLE Portfolios (
    id SERIAL PRIMARY KEY,
    parent_id INTEGER,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    created_date DATE NOT NULL,
    updated_date DATE,
    FOREIGN KEY (parent_id) REFERENCES Portfolios(id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (created_date) REFERENCES Dates(date),
    FOREIGN KEY (updated_date) REFERENCES Dates(date),
    UNIQUE(user_id, parent_id, name)
);

CREATE TABLE Positions (
    id SERIAL PRIMARY KEY,
    portfolio_id INTEGER NOT NULL,
    instrument_type_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    cost_basis REAL,
    unrealised_gain_loss REAL,
    gain_loss REAL,
    opened_date DATE,
    updated_date DATE,
    closed_date DATE,
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(id),
    FOREIGN KEY (instrument_type_id) REFERENCES InstrumentTypes(id),
    FOREIGN KEY (instrument_id) REFERENCES Instruments(id),
    FOREIGN KEY (opened_date) REFERENCES Dates(date),
    FOREIGN KEY (updated_date) REFERENCES Dates(date),
    FOREIGN KEY (closed_date) REFERENCES Dates(date),
    UNIQUE(portfolio_id, account_id, asset_id)
);

CREATE TABLE TransactionClasses (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE TransactionTypes (
    id SERIAL PRIMARY KEY,
    class_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    FOREIGN KEY (class_id) REFERENCES TransactionClasses(id)
);
CREATE TABLE Transactions (
    id SERIAL PRIMARY KEY,
    type_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    date DATE NOT NULL,
    price REAL,
    fee REAL,
    fee_currency TEXT,
    FOREIGN KEY (type_id) REFERENCES TransactionTypes(id),
    FOREIGN KEY (position_id) REFERENCES Positions(id),
    FOREIGN KEY (date) REFERENCES Dates(date)
);

CREATE TABLE Indicators (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);
CREATE TABLE Signals (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);
CREATE TABLE Rules (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE DailyStockData (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    stock_id INTEGER NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    FOREIGN KEY (stock_id) REFERENCES Stocks(id),
    FOREIGN KEY (date) REFERENCES Dates(date),
    UNIQUE(stock_id, date)
);
CREATE TABLE DailyPositionData (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    position_id INTEGER NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (position_id) REFERENCES Positions(id),
    FOREIGN KEY (date) REFERENCES Dates(date),
    UNIQUE(portfolio_id, date)
); -- separate necessary and unnecessary data
CREATE TABLE DailyIndicatorData (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    indicator_id INTEGER NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (date) REFERENCES Dates(date),
    FOREIGN KEY (indicator_id) REFERENCES Indicators(id),
    UNIQUE(indicator_id, date)
);
CREATE TABLE DailySignalData (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    signal_id INTEGER NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (date) REFERENCES Dates(date),
    FOREIGN KEY (signal_id) REFERENCES Signals(id)
);