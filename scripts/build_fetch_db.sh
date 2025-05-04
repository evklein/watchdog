#!/bin/bash

fetch_db=${WATCHDOG_FETCH_DB_LOC/#\~/$HOME}
echo "Building database at location $fetch_db"

if [ -f "$fetch_db" ]; then
	rm "$fetch_db"
	echo "Database removed. Cleared to rebuild from scatch."
else
	echo "Warning: $fetch_db does not exist, nothing to remove"
fi

echo "Creating Table - Fetch"
sqlite3 $fetch_db < sql/CreateTableWatchdogDataFetchRecords.sql

echo "Database successfully created at location $fetch_db."

