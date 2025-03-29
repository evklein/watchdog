import requests
import os
import sqlite3
import time

EDGAR_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_EDGAR_DB_DIR'))
print(f'DB Connection string: {EDGAR_DB_CONNECTION_STR}')
HEADERS = {
    'User-Agent': 'Evan Klein (Indiana University) evklein@iu.edu',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.sec.gov'
}

## Make database connections
sqliteConnection = sqlite3.connect(EDGAR_DB_CONNECTION_STR)
cursor = sqliteConnection.cursor()

## Get CIKs from database
retrieve_cik_command = 'SELECT CIK FROM SECEntity'
cursor.execute(retrieve_cik_command)
ciks_raw = cursor.fetchall()
ciks = [cik_obj[0] for cik_obj in ciks_raw]

## Grab JSON from EDGAR - pull out what we need an insert it into table
for i, cik in enumerate(ciks):
    edgar_req = requests.get(f'https://data.sec.gov/submissions/CIK{cik}.json', headers = HEADERS)
    edgar_res = edgar_req.json()
    print(edgar_res['name'])
    update_entity_row_command = f'''
UPDATE SECEntity SET
    Name = '{edgar_res["name"]}',
    EntityType = '{edgar_res["entityType"]}',
    IncorporationState = '{edgar_res["stateOfIncorporation"]}',
    PhoneNumber = '{edgar_res["phone"]}',
    Address = '{edgar_res["addresses"]["business"]["street1"]}'
WHERE CIK = '{cik}';
    '''
    print(update_entity_row_command)
    cursor.execute(update_entity_row_command)
    sqliteConnection.commit()
    if i % 10 == 0: # Timing fun - SEC asks for no more than 10 req/sec.
        time.sleep(1)

## Terminate database connection
cursor.close()
