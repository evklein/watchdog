import os
import requests
from datetime import datetime
from pymongo import MongoClient
from collections import namedtuple

BLS_API_KEY = os.environ.get('WATCHDOG_BLS_API_KEY')
MONGO_HOST = os.environ.get('WATCHDOG_MONGO_DB_HOST')
MONGO_PORT = os.environ.get('WATCHDOG_MONGO_DB_PORT')
SERIES_ID = 'CUUR0000SA0'
START_YEAR = 1960
END_YEAR = datetime.now().year
YEAR_LIMIT_PER_REQ = 10

ConsumerPriceIndexRecord = namedtuple('ConsumerPriceIndexRecord', ['date', 'cpi'])

def ExtractCPIData():
    print('Extracting CPI Data from BLS')
    aggregated_cpi_records = []
    for i in range(START_YEAR, END_YEAR, YEAR_LIMIT_PER_REQ): # Limit to 10 years - BLS API won't return more than 10 years at a time, so we break up the requests.
        chunk_start = i
        chunk_end = min(i + YEAR_LIMIT_PER_REQ, END_YEAR)
        req_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/{SERIES_ID}?startyear={chunk_start}&endyear={chunk_end}&registrationkey={BLS_API_KEY}'
        bls_req = requests.get(req_url)
        if bls_req.status_code == 200:
            cpi_data_by_month = bls_req.json()['Results']['series'][0]['data']
            aggregated_cpi_records.extend(cpi_data_by_month)
    print(f'CPI data extracted. {len(aggregated_cpi_records)} months worth of data found.')
    return aggregated_cpi_records

def TransformCPIData(aggregated_data):
    print('Transforming CPI data.')
    print(aggregated_data)
    return [
        ConsumerPriceIndexRecord(
            datetime.strptime(f'{record["year"]}-{record["period"][1:]}-15', '%Y-%m-%d'),
            float(record['value'])
        )
        for record in aggregated_data
    ]

def LoadCPIData(transformed_data):
    print('Inserting transformed data into Mongo.')
    mongo_client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    mongo_client['economic-data']['cpi'].insert_many(transformed_data)

if __name__ == '__main__':
    cpi_records = ExtractCPIData()
    transformed_records = TransformCPIData(cpi_records)
    LoadCPIData(transformed_records)
