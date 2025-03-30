import os
import requests

BLS_API_KEY = os.environ.get('WATCHDOG_BLS_API_KEY')

def ExtractCPIData():
    bls_req = requests.get(f'https://api.bls.gov/publicAPI/v2/timeseries/data/{series}')    
    cpi_data = bls_req.json()
    print(cpi_data)

if __name__ == 'main':
    ExtractCPIData()