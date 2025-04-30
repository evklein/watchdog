CREATE TABLE BLSTimeSeries(
    SeriesID NVARCHAR(50) PRIMARY KEY,
    Title NVARCHAR(250),
    Seasonality NVARCHAR(250),
    SurveyName NVARCHAR(250),
    SurveyAbbreviation NVARCHAR(20),
    MeasureDataType NVARCHAR(250),
    CommerceIndustry NVARCHAR(250),
    Occupation NVARCHAR(250),
    OccupationWorkClass NVARCHAR(250),
    Area NVARCHAR(250)
);
