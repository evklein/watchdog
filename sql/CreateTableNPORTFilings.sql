CREATE TABLE NPORTFilings(
    FilingId CHAR(50) PRIMARY KEY NOT NULL,
    EntityId CHAR(200) NOT NULL, 
    SeriesClassCompositeKey CHAR(50) NOT NULL, 
    PeriodStart DATE NOT NULL,
    PeriodEnd DATE NOT NULL,
    TotalAssetsValue FLOAT,
    TotalLiabilitiesValue FLOAT,
    FOREIGN KEY (EntityId) REFERENCES SECEntities(EntityId),
    FOREIGN KEY (SeriesClassCompositeKey) REFERENCES SeriesClasses(SeriesClassCompositeKey)
);
