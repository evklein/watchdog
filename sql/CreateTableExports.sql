CREATE TABLE ExportRecord (
    Id INTEGER PRIMARY KEY,
    DistrictId INTEGER,
    DistrictName VARCHAR(200),
    CommodityId VARCHAR(50),
    CommodityDescription VARCHAR(500),
    ValueForMonth FLOAT,
    ValueYearToDate FLOAT,
    Month INTEGER,
    Year INTEGER
);
