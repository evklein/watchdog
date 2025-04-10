#!/bin/bash

trade_db=${WATCHDOG_TRADE_DB_LOC/#\~/$HOME}
echo "Building database at location $trade_db"

if [ -f "$trade_db" ]; then
    rm "$trade_db"
    echo "Database removed. Cleared to rebuild from scratch."
else
    echo "Warning: $trade_db does not exist. Nothing to remove."
fi

echo "Creating Table - Imports"
sqlite3 $trade_db < sql/CreateTableImports.sql

echo "Create Table - Exports"
sqlite3 $trade_db < sql/CreateTableExports.sql

echo "Database successfully created at location $trade_db. Ready for import."
