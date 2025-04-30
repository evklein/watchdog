bls_db=${WATCHDOG_BLS_DB_LOC/#\~/$HOME}

echo "Seeding BLS Time Series values for database located at $bls_db."

if [ -f "$bls_db" ]; then
	sqlite3 $bls_db < sql/SeedTableBLSSeries.sql
else
	echo "Warning: $bls_db does not exist, nothing to seed."
fi

echo "Time series IDs seeded."
