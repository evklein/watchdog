CREATE TABLE NPORTFilings(
    FilingId CHAR(50) PRIMARY KEY NOT NULL,
    EntityId CHAR(200) FOREIGN KEY REFERENCES SECEntities(EntityId),  
    SeriesClassCompositeKey CHAR(50) FOREIGN KEY REFERENCES SeriesClasses(SeriesClassCompositeKey),
    PeriodStart DATE NOT NULL,
    PeriodEnd DATE NOT NULL,
    TotalAssetsValue FLOAT,
    TotalLiabilitiesValue FLOAT
);