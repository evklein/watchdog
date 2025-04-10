CREATE TABLE ImportRecord (
    Id INTEGER PRIMARY KEY,
    CountryCode NVARCHAR(200),
    CountryName NVARCHAR(200),
    EndUseCode NVARCHAR(500),
    EndUseDescription NVARCHAR(500),
    ValueForMonth FLOAT,
    ValueYearToDate FLOAT,
    Month INTEGER,
    Year INTEGER
);
