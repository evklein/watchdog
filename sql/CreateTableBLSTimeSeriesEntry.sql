CREATE TABLE TimeSeriesEntry(
    Year INTEGER,
    TimeSeriesID NVARCHAR(50),
    Period NVARCHAR(5),
    PeriodName NVARCHAR(20),
    Value FLOAT,
    FOREIGN KEY (TimeSeriesID) REFERENCES BLSTimeSeries(SeriesID)
)
