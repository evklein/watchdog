CREATE TABLE NPORTFilings(
    FilingId CHAR(50) PRIMARY KEY NOT NULL,
    EntityCIK CHAR(200) FOREIGN KEY REFERENCES SECEntities(CIK),  
    SeriesClassCompositeKey CHAR(50) FOREIGN KEY REFERENCES SeriesClasses(SeriesClassCompositeKey),
    ReportingPeriodEnd DATE NOT NULL,
    TotalAssetsValue FLOAT,
    TotalLiabilitiesValue FLOAT
);