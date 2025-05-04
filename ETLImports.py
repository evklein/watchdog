import os
import requests
import sqlite3
import datetime
from requests.exceptions import ConnectionError

TRADE_DB_CONNECTION_STRING = os.path.expanduser(os.environ.get('WATCHDOG_TRADE_DB_LOC'))
FETCH_DB_CONNECTION_STRING = os.path.expanduser(os.environ.get('WATCHDOG_FETCH_DB_LOC'))

CENSUS_API_KEY = os.environ.get('WATCHDOG_CENSUS_API_KEY')

def FetchImportsForMonth(sql_connection, cursor, month, year, fetch_sql_connection, fetch_cursor):
    pad_month = f'{month}'.rjust(2, '0')
    print(f'Fetching import record for {pad_month}-{year}')
    req_url = f'https://api.census.gov/data/timeseries/intltrade/imports/enduse?get=CTY_CODE,CTY_NAME,I_ENDUSE,I_ENDUSE_LDESC,GEN_VAL_MO,CON_VAL_MO&time={year}-{pad_month}&key={CENSUS_API_KEY}'
    for attempt in range(3):
        try:
            res = requests.get(req_url)
            res.raise_for_status()
            break
        except (ConnectionError, requests.exceptions.RequestException) as e:
            if attempt == 2:
                print(f'Failed. {e}')
                return
            else:
                print('Connection failed - retrying...')
                time.sleep(10)

    data = res.json()[1:] # Filter out first result, as it's just column labels.
    print(f'{len(data)} records found. Importing')
    query = 'INSERT OR REPLACE INTO ImportRecords(CountryCode, CountryName, EndUseCode, EndUseDescription, ValueForMonth, ValueYearToDate, Month, Year) VALUES\n'
    for i, record in enumerate(data):
        country_code = record[0] if record[0] != '-' else None
        country_name = record[1].replace('\'', '')
        enduse_code = int(record[2]) if record[2] != '-' else None
        enduse_description = record[3]
        value_month = int(record[4])
        value_ytd = int(record[5])
        #trailing_comma = ',\n' if i < len(data) - 1 else '\n'
        trailing_marker = ',\n' if i < len(data) - 1 else '\n'
        query += f'(\'{country_code}\', \'{country_name}\', \'{enduse_code}\', \'{enduse_description}\', {value_month}, {value_ytd}, {month}, {year}){trailing_marker}'
    query += ';'
    cursor.execute(query)
    sql_connection.commit()

    fetch_query = f'INSERT INTO FetchRecords(Source, Destination, NewRecordsAdded, OperationRan) VALUES (\'Census API (Imports) {pad_month}-{year}\', \'Trade Database - Imports Table\', {len(data)}, \'{datetime.datetime.now()}\');'
    fetch_cursor.execute(fetch_query)
    fetch_sql_connection.commit()

if __name__ == "__main__":
    print('Fetching and loading imports!')
    sql_connection = sqlite3.connect(TRADE_DB_CONNECTION_STRING)
    fetch_sql_connection = sqlite3.connect(FETCH_DB_CONNECTION_STRING)
    cursor = sql_connection.cursor()
    fetch_cursor = fetch_sql_connection.cursor()
    now = datetime.datetime.now()

    # Fetch for each month
    for i in range(2013, now.year + 1):
          for j in range(1, 13):
              if i == now.year and j == now.month:
                  break
              FetchImportsForMonth(sql_connection, cursor, j, i, fetch_sql_connection, fetch_cursor) 
