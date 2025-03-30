CREATE TABLE FundHoldings(
    HoldingId INTEGER PRIMARY KEY AUTOINCREMENT,
    LEI CHAR(50) NOT NULL,
    SecurityName CHAR(200) NOT NULL,
    SecurityTitle CHAR(200) NOT NULL,
    Balance FLOAT,
    ValueUSD FLOAT,
    PercentOfHoldings FLOAT,
    AssetCategory CHAR(50),
    NPORTFilingId CHAR(50) NOT NULL,
    FOREIGN KEY (NPORTFilingId) REFERENCES NPORTFilings(FilingId)
);