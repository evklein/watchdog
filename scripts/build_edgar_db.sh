#!/bin/bash

edgar_db=${WATCHDOG_EDGAR_DB_LOC/#\~/$HOME}
echo "Building database at location $edgar_db"

if [ -f "$edgar_db" ]; then
	rm "$edgar_db"
	echo "Database removed. Cleared to rebuild from scatch."
else
	echo "Warning: $edgar_db does not exist, nothing to remove"
fi

echo "Creating Table - SECEntities"
sqlite3 $edgar_db < sql/CreateTableSECEntities.sql

echo "Creating Table - SeriesClasses"
sqlite3 $edgar_db < sql/CreateTableSeriesClasses.sql

echo "Creating Table - NPORTFilings"
sqlite3 $edgar_db < sql/CreateTableNPORTFilings.sql

echo "Creating Table - FundHoldings"
sqlite4 $edgar_db < sql/CreateTableFundHoldings.sql

echo "Database successfully created at location $edgar_db"

bash ./seed_edgar_ciks.sh