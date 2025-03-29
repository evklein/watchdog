CREATE TABLE SECEntity(
    CIK CHAR(150) PRIMARY KEY NOT NULL,
    NAME CHAR(200),
    EntityType CHAR(200),
    IncorporationState CHAR(20),
    PhoneNumber CHAR(20),
    Address CHAR(200)
);