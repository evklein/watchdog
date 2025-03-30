edgar_db=${WATCHDOG_EDGAR_DB_LOC/#\~/$HOME}

echo "Seeding SEC Entities CIK values for database located at $edgar_db."

if [ -f "$edgar_db" ]; then
	sqlite3 $edgar_db < sql/SeedTableSECEntities.sql
else
	echo "Warning: $edgar_db does not exist, nothing to seed."
fi

echo "CIKs seeded."