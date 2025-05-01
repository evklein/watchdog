CREATE TABLE FetchRecords(
    Id INTEGER PRIMARY KEY,
    Source NVARCHAR(50) NOT NULL,
    Destination NVARCHAR(50) NOT NULL,
    NewRecordsAdded INTEGER,
    OperationRan DATE
)
