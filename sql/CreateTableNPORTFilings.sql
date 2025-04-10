CREATE TABLE NPORTFilings(
    FilingId CHAR(50) PRIMARY KEY NOT NULL,
    EntityCIK CHAR(200),
    SeriesClassCompositeKey CHAR(50),
    ReportingPeriodEnd DATE NOT NULL,
    ReportingPeriodDate DATE NOT NULL,
    TotalAssetsValue FLOAT,
    TotalLiabilitiesValue FLOAT,
    FOREIGN KEY (EntityCIK) REFERENCES SECEntities(CIK),
    FOREIGN KEY (SeriesClassCompositeKey) REFERENCES SeriesClasses(SeriesClassCompositeKey)
);