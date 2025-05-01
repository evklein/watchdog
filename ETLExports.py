import os
import time
import requests
import sqlite3
import datetime
from requests.exceptions import ConnectionError

TRADE_DB_CONNECTION_STRING = os.path.expanduser(os.environ.get('WATCHDOG_TRADE_DB_LOC'))
CENSUS_API_KEY = os.environ.get('WATCHDOG_CENSUS_API_KEY')
FETCH_DB_CONNECTION_STRING = os.path.expanduser(os.environ.get('WATCHDOG_FETCH_DB_LOC'))

def FetchImportsForMonth(sql_connection, cursor, month, year, fetch_sql_connection, fetch_cursor):
    pad_month = f'{month}'.rjust(2, '0')
    print(f'Fetching export record for {pad_month}-{year}')
    req_url = f'https://api.census.gov/data/timeseries/intltrade/exports/hs?get=E_COMMODITY,E_COMMODITY_LDESC,ALL_VAL_MO,VES_VAL_MO,AIR_VAL_MO,CC_MO&YEAR={year}&MONTH={pad_month}&key={CENSUS_API_KEY}'
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
    query = 'INSERT OR REPLACE INTO ExportRecords(CommodityId, CommodityDescription, TotalValueForMonth, VesselValueForMonth, AirValueForMonth, CardCount, Month, Year) VALUES\n'
    for i, record in enumerate(data):
        commodity_code = record[0]
        commodity_description = record[1].replace('\'', '')
        value_total_month = int(record[2])
        value_vessel_month = int(record[3])
        value_air_month = int(record[4])
        card_count_month = int(record[5])
        value_month = int(record[7])
        value_year = int(record[6])
        trailing_marker = ',\n' if i < len(data) - 1 else '\n'
        query += f'(\'{commodity_code}\', \'{commodity_description}\', {value_total_month}, {value_vessel_month}, {value_air_month}, {card_count_month}, {value_month}, {value_year}){trailing_marker}'
    query += ';'
    cursor.execute(query)
    sql_connection.commit()
    fetch_query = f'INSERT INTO FetchRecords(Source, Destination, NewRecordsAdded, OperationRan) VALUES (\'Census API (Exports) {pad_month}-{year}\', \'Trade Database - Exports Table\', {len(data)}, \'{datetime.datetime.now()}\');'
    print(fetch_query)
    fetch_cursor.execute(fetch_query)
    fetch_sql_connection.commit()



if __name__ == "__main__":
    print('Fetching and loading exports!')
    trade_sql_connection = sqlite3.connect(TRADE_DB_CONNECTION_STRING)
    fetch_sql_connection = sqlite3.connect(FETCH_DB_CONNECTION_STRING)
    trade_cursor = trade_sql_connection.cursor()
    fetch_cursor = fetch_sql_connection.cursor()
    now = datetime.datetime.now()

    # Fetch for each month
    for i in range(2013, now.year + 1):
          for j in range(1, 13):
              if i == now.year and j == now.month:
                  break
              FetchImportsForMonth(trade_sql_connection, trade_cursor, j, i, fetch_sql_connection, fetch_cursor)
              
