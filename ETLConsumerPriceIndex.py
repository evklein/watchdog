import os
import requests
from datetime import datetime

BLS_API_KEY = os.environ.get('WATCHDOG_BLS_API_KEY')
SERIES_ID = 'CUUR0000SA0'
START_YEAR = 1960
END_YEAR = datetime.now().year
YEAR_LIMIT_PER_REQ = 10

def ExtractCPIData():
    for i in range(START_YEAR, END_YEAR, YEAR_LIMIT_PER_REQ): # Limit to 10 years - BLS API won't return more than 10 years at a time, so we break up the requests.
        chunk_start = i
        chunk_end = min(i + YEAR_LIMIT_PER_REQ, END_YEAR)
        req_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/{SERIES_ID}?startyear={chunk_start}&endyear={chunk_end}'
        bls_req = requests.get(req_url)
        if bls_req.status_code == 200:
            cpi_data_by_month = bls_req.json()['Results']['series'][0]['data']
            for cpi_recording in cpi_data_by_month:
                print(f'{cpi_recording["periodName"]} {cpi_recording["year"]}: {cpi_recording["value"]}')

if __name__ == '__main__':
    ExtractCPIData()
