import requests
import os
import sqlite3
import time
import random

BLS_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_BLS_DB_LOC'))
BLS_API_KEY = os.environ.get('WATCHDOG_BLS_API_KEY')
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

if __name__ == "__main__":
    sql_connection = sqlite3.connect(BLS_DB_CONNECTION_STR)
    cursor = sql_connection.cursor()
    # Grab survey types
    res = requests.get(f'https://api.bls.gov/publicAPI/v2/surveys?registrationKey={BLS_API_KEY}')
    surveys = res.json()['Results']['survey']
    length = 0
    for survey in surveys:
        time.sleep(.25)
        survey_abrv = survey['survey_abbreviation']
        survey_res = requests.get(f'https://api.bls.gov/publicAPI/v2/timeseries/popular?survey={survey_abrv}&registrationKey={BLS_API_KEY}')
        series_list = survey_res.json()['Results']['series']
        length += len(series_list)
        if series_list[0] is not None:
            #print(f'{len(series_list)} series found for {survey_abrv}')
            pass
    print(f'{length} series found.')
