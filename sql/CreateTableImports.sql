CREATE TABLE ImportRecords (
    Id INTEGER PRIMARY KEY,
    CountryCode NVARCHAR(50),
    CountryName NVARCHAR(200),
    EndUseCode INTEGER,
    EndUseDescription NVARCHAR(500),
    ValueForMonth INTEGER,
    ValueYearToDate INTEGER,
    Month INTEGER,
    Year INTEGER
);
