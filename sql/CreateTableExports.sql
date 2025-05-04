CREATE TABLE ExportRecords (
    Id INTEGER PRIMARY KEY,
    CommodityId VARCHAR(50),
    CommodityDescription VARCHAR(500),
    TotalValueForMonth INTEGER,
    VesselValueForMonth INTEGER,
    AirValueForMonth INTEGER,
    CardCount INTEGER,
    Month INTEGER,
    Year INTEGER
);
