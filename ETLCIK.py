import requests
import os
import sqlite3
import time
import random

EDGAR_CIK_LIST_LOC = os.path.expanduser(os.environ.get('WATCHDOG_EDGAR_CIK_LIST_LOC'))
EDGAR_CIK_TARGETS_LOC = os.path.expanduser(os.environ.get('WATCHDOG_EDGAR_CIK_TARGETS_LOC'))
EDGAR_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_EDGAR_DB_LOC'))
HEADERS = {
    'User-Agent': 'Evan Klein (Indiana University) evklein@iu.edu',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.sec.gov'
}

REQ_LIMIT_PER_SEC = 10
REQ_LIMIT_PAUSE_INTERVAL = 1
CIK_LIMIT = 1000

running_req_count = 0
running_cik_count = 0

def FetchSubmissions(cik, cursor, sql_connection):
    global running_cik_count
    global running_req_count

    running_req_count += 1
    if running_req_count % REQ_LIMIT_PER_SEC == 0:
        print(f'Requests made: {running_req_count}, Funds identified: {running_cik_count}')
        #time.sleep(REQ_LIMIT_PAUSE_INTERVAL)
    edgar_res = requests.get(f'https://data.sec.gov/submissions/CIK{cik}.json', headers=HEADERS)

    if "NPORT-P" in edgar_res.text:
        running_cik_count += 1
        data = edgar_res.json()
        update_row_command = f'''
            INSERT OR REPLACE INTO SECEntities(Name, EntityType, IncorporationState, PhoneNumber, Address, CIK) VALUES(
                '{data["name"].replace("'", "")}',
                '{data["entityType"]}',
                '{data["stateOfIncorporation"]}',
                '{data["phone"]}',
                '{data["addresses"]["business"]["street1"]}',
                '{cik}'
            );
        '''
        print(update_row_command)
        cursor.execute(update_row_command)
        sql_connection.commit()

if __name__ == "__main__":
    sql_connection = sqlite3.connect(EDGAR_DB_CONNECTION_STR)
    cursor = sql_connection.cursor()
    with open(EDGAR_CIK_TARGETS_LOC) as cik_targets_file:
        cik_targets = cik_targets_file.read().splitlines()

        with open(EDGAR_CIK_LIST_LOC) as cik_list_file:
            for i, cik_listing in enumerate(cik_list_file):
                print(i)
                for j, target in enumerate(cik_targets):
                    if target in cik_listing:
                        markers = [i for i, char in enumerate(cik_listing) if char == ':']
                        cik = cik_listing[(markers[-2] + 1):markers[-1]]
                        FetchSubmissions(cik, cursor, sql_connection)
