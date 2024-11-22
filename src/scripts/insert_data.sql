WITH RECURSIVE DateSeries AS (
    SELECT '1990-01-01' AS dt, CAST('1990-01-01' AS DATE) AS date  -- Starting date
    UNION ALL
    SELECT
        DATE(dt, '+1 day'),  -- Add 1 day to the previous date
        DATE(dt, '+1 day')
    FROM DateSeries
    WHERE dt < '2090-12-31'  -- End date
)
INSERT INTO Dates (date, day_of_week, week_number, month, quarter, year, is_weekend)
    SELECT
        date,
        STRFTIME('%w', date),  -- Day of week (0-6, Sunday is 0)
        STRFTIME('%W', date),  -- Week number (0-53)
        STRFTIME('%m', date),  -- Month (01-12)
        CAST((STRFTIME('%m', date) - 1) / 3 + 1 AS INT),  -- Quarter (1-4)
        STRFTIME('%Y', date),  -- Year
        CASE WHEN STRFTIME('%w', date) IN ('0', '6') THEN 1 ELSE 0 END,  -- Is weekend (1 for True, 0 for False)
    FROM DateSeries
;

INSERT INTO Sectors (name) VALUES (
    ('FINANCE'),
    ('ENERGY'),
    ('CONSUMER STAPLES'),
    ('HEALTH CARE'),
    ('INFORMATION TECHNOLOGY')
);

INSERT INTO AssetClasses (id, name, description) VALUES
    (1, 'equity', 'ownership stake in a company or asset'),
    (2, 'fixed income', 'obligation to repay borrowed funds'),
    (3, 'cash and cash equivalents', 'highly liquid currency assets readily convertible to cash'),
    (4, 'derivatives', 'financial contracts that derive their value from an underlying asset, such as options or futures'),
    (5, 'real estate', 'real estate assets including land, buildings, and other real estate'),
    (6, 'commodities', 'raw materials or primary agricultural products traded on exchanges, like oil, gold, or wheat'),
    (7, 'alternative', 'any financial instrument not categorised above, including collectibles, precious metals, or alternative investments')
;
INSERT INTO AssetTypes (class_id, name, description) VALUES
    (1, 'Stock', 'Represents ownership in a company or asset'),
    -- (1, 'Common Stock', 'Represents ownership in a company with voting rights and potential for dividends.'),
    -- (1, 'Preferred Stock', 'Represents ownership in a company with priority for dividends but typically no voting rights.'),
    (1, 'ETF', 'Exchange-traded fund, a basket of securities traded on an exchange like a stock.'),
    (1, 'Mutual Fund', 'Investment fund that pools money from multiple investors to invest in a diversified portfolio.'),
    (2, 'Bond', 'Debt security that obligates the issuer to pay interest and principal at maturity.'),
    (2, 'Corporate Bond', 'Bond issued by a corporation to raise capital.'),
    (2, 'Government Bond', 'Bond issued by a government to finance public spending.'),
    (2, 'Municipal Bond', 'Bond issued by a state or local government.'),
    (3, 'Currency', 'Government-issued legal tender used as a medium of exchange.'),
    (3, 'Money Market Instruments', 'Short-term debt securities with high liquidity, such as Treasury bills and commercial paper.'),
    (4, 'Residential Property', 'Land and buildings used for residential purposes, such as houses and apartments.'),
    (4, 'Commercial Property', 'Land and buildings used for commercial purposes, such as office buildings and retail stores.'),
    (4, 'Industrial Property', 'Land and buildings used for industrial purposes, such as factories and warehouses.'),
    (5, 'Precious Metals', 'Rare and valuable metals like gold, silver, and platinum.'),
    (5, 'Energy', 'Commodities related to energy production, such as crude oil and natural gas.'),
    (5, 'Agricultural Products', 'Raw materials derived from agriculture, such as grains, livestock, and softs (coffee, sugar, etc.).'),
    (6, 'Option', 'Contract giving the holder the right, but not the obligation, to buy or sell an asset at a specific price.'),
    (6, 'Future', 'Contract obligating parties to transact an asset at a predetermined price and date.'),
    (6, 'Swap', 'Agreement to exchange cash flows or assets based on different financial instruments.'),
    (7, 'Collectibles', 'Items of value collected for their rarity or historical significance, such as art, stamps, or coins.'),
    (7, 'Cryptocurrency', 'Digital or virtual currency that uses cryptography for security.')
;

INSERT INTO TransactionClasses (id, name, description) VALUES
    (1, 'trade', 'buying or selling of securities'),
    (2, 'cash flow', 'deposits, withdrawals, and transfers'),
    (3, 'income', 'dividends and interest payments'),
    (4, 'expense', 'fees, taxes, and other expenses')
;
-- INSERT INTO TransactionTypes (class_id, name, description) VALUES
--     (1, 'buy', 'Purchase of an asset.'),
--     (1, 'sell', 'Sale of an asset.'),
--     (2, 'deposit', 'Adding cash into an account.'),
--     (2, 'withdrawal', 'Removing cash from an account.'),
--     (2, 'transfer', 'Moving cash between accounts.'),
--     (3, 'interest', 'Payment received for lending funds or holding interest-bearing assets.'),
--     (3, 'dividend', 'Payment made by a company to its shareholders.'),
--     (4, 'fee', 'Fee charged for a transaction or service.'),
--     (4, 'tax', 'Tax paid on investment income or gains.')
-- --    ('short sell', 'Sale of a borrowed asset.'),
-- --    ('cover short', 'Purchase of an asset to close a short sell.'),
-- ;