#!/bin/bash

bls_db=${WATCHDOG_BLS_DB_LOC/#\~/$HOME}
echo "Building database at location $bls_db"

if [ -f "$bls_db" ]; then
	rm "$bls_db"
	echo "Database removed. Cleared to rebuild from scatch."
else
	echo "Warning: $bls_db does not exist, nothing to remove"
fi

echo "Creating Table - Time Series"
sqlite3 $bls_db < sql/CreateTableBLSTimeSeries.sql

echo "Creating Table - Time Series Entry"
sqlite3 $bls_db < sql/CreateTableBLSTimeSeriesEntry.sql

echo "Database successfully created at location $bls_db."

