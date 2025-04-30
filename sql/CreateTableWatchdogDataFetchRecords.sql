CREATE TABLE FetchRecord(
    Id INTEGER PRIMARY KEY,
    Source NVARCHAR(50) NOT NULL,
    NewRecordsAdded INTEGER,
    OperationRan DATE
)
