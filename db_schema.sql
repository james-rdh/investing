------------ INSTRUMENTS ------------
CREATE TABLE IF NOT EXISTS InstrumentClasses (
    id INTEGER PRIMARY KEY,
    class TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE IF NOT EXISTS InstrumentTypes (
    id INTEGER PRIMARY KEY,
    class_id INTEGER NOT NULL,
    type TEXT NOT NULL UNIQUE,
    description TEXT,
    FOREIGN KEY (class_id) REFERENCES InstrumentClasses(id)
);
CREATE TABLE IF NOT EXISTS Instruments (
    id INTEGER PRIMARY KEY,
    class_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    exchange TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    currency TEXT NOT NULL, -- separate table?
    sector TEXT, -- separate table?
    country TEXT, -- separate table?
    isin TEXT,
    data_source TEXT,
    name TEXT,
    description TEXT,
    FOREIGN KEY (class_id) REFERENCES InstrumentClasses(id),
    FOREIGN KEY (type_id) REFERENCES InstrumentTypes(id),
    UNIQUE(symbol, exchange)
);

------------ POSITIONS ------------
CREATE TABLE IF NOT EXISTS PositionTypes (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE IF NOT EXISTS Positions (
    id INTEGER PRIMARY KEY,
    type_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    FOREIGN KEY (type_id) REFERENCES PositionTypes(id),
    FOREIGN KEY (instrument_id) REFERENCES Instrument(id),
    UNIQUE(type_id, instrument_id)
);

------------ ACCOUNTS ------------
CREATE TABLE IF NOT EXISTS AccountTypes (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE IF NOT EXISTS AccountInstitutions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE IF NOT EXISTS Accounts (
    id INTEGER PRIMARY KEY,
    type_id INTEGER NOT NULL,
    institution_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    FOREIGN KEY (type_id) REFERENCES AccountTypes(id),
    FOREIGN KEY (institution_id) REFERENCES AccountInstitutions(id)
);

------------ ACCOUNT POSITIONS ------------
CREATE TABLE IF NOT EXISTS AccountPositions (
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    created_date TEXT NOT NULL,
    updated_date TEXT NOT NULL,
    removed_date TEXT,
    FOREIGN KEY (account_id) REFERENCES Accounts(id),
    FOREIGN KEY (position_id) REFERENCES Positions(id),
    UNIQUE(account_id, position_id)
);

------------ TRANSACTIONS ------------
CREATE TABLE IF NOT EXISTS TransactionTypes (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE IF NOT EXISTS Transactions (
    id INTEGER PRIMARY KEY,
    type_id INTEGER NOT NULL,
    account_position_id INTEGER NOT NULL,
    date TEXT,
    price REAL,
    cost REAL,
    amount REAL,
    FOREIGN KEY (type_id) REFERENCES TransactionTypes(id),
    FOREIGN KEY (account_position_id) REFERENCES AccountPositions(id)
);

------------ USERS ------------
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    created_date TEXT NOT NULL,
    last_login_date TEXT
);
CREATE TABLE IF NOT EXISTS UserPreferences (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,
    currency TEXT,
    risk_tolerance REAL,
    dark_mode TEXT,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

------------ WATCHLISTS ------------
CREATE TABLE Watchlists (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    created_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (instrument_id) REFERENCES Instruments(id),
    UNIQUE(user_id, instrument_id)
);

------------ GOALS ------------
CREATE TABLE Goals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    goal_type TEXT NOT NULL,
    target_value NUMERIC,
    target_date TEXT,
    is_completed BOOLEAN DEFAULT FALSE,
    created_date TEXT NOT NULL,
    updated_date TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

------------ ANALYSES ------------
CREATE TABLE IF NOT EXISTS Analyses (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    code TEXT NOT NULL,
    created_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    UNIQUE(user_id, name)
);

------------ GEOGRAPHIC AREAS ------------
CREATE TABLE IF NOT EXISTS GeographicAreas (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER,
    name TEXT NOT NULL,
    area_type TEXT NOT NULL,
    geo_data TEXT,
    FOREIGN KEY (parent_id) REFERENCES GeographicAreas(id)
);

------------ TIME SERIES ------------
CREATE TABLE IF NOT EXISTS DailyInstrumentData (
    id INTEGER PRIMARY KEY,
    instrument_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    FOREIGN KEY (instrument_id) REFERENCES Instruments(id),
    UNIQUE(instrument_id, date)
);
CREATE TABLE IF NOT EXISTS DailyPositionData (
    id INTEGER PRIMARY KEY,
    position_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    market_value REAL NOT NULL,
    cost_basis REAL,
    daily_gain_loss REAL,
    unrealised_gain_loss REAL,
    FOREIGN KEY (position_id) REFERENCES Positions(id),
    UNIQUE(position_id, date)
);
CREATE TABLE IF NOT EXISTS DailyAccountData (
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    market_value REAL NOT NULL,
    cost_basis REAL,
    daily_gain_loss REAL,
    unrealised_gain_loss REAL,
    FOREIGN KEY (account_id) REFERENCES Accounts(id),
    UNIQUE(account_id, date)
);
CREATE TABLE IF NOT EXISTS DailyRegionData (
    id INTEGER PRIMARY KEY,
    region_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (region_id) REFERENCES Regions(id),
    UNIQUE(region_id, date)
);
CREATE TABLE IF NOT EXISTS DailyNewsData (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    description TEXT NOT NULL
);
