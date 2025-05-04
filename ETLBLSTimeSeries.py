import requests
import os
import sqlite3
import time
import random
import datetime

BLS_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_BLS_DB_LOC'))
FETCH_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_FETCH_DB_LOC'))
BLS_API_KEY = os.environ.get('WATCHDOG_BLS_API_KEY')
REQ_PAUSE_INTERVAL = 0.25 # In seconds

if __name__ == "__main__":
    sql_connection = sqlite3.connect(BLS_DB_CONNECTION_STR)
    fetch_connection = sqlite3.connect(FETCH_DB_CONNECTION_STR)
    cursor = sql_connection.cursor()
    fetch_cursor = fetch_connection.cursor()
    
    # Grab survey types
    res = requests.get(f'https://api.bls.gov/publicAPI/v2/surveys?registrationKey={BLS_API_KEY}')
    surveys = res.json()['Results']['survey']
    series_ids = []

    # Fetch 25 most popular series for each survey
    for survey in surveys:
        time.sleep(REQ_PAUSE_INTERVAL)
        survey_abrv = survey['survey_abbreviation']
        survey_res = requests.get(f'https://api.bls.gov/publicAPI/v2/timeseries/popular?survey={survey_abrv}&registrationKey={BLS_API_KEY}')
        series_list = survey_res.json()['Results']['series']
        if series_list[0] is not None:
            print(f'{len(series_list)} series found for {survey_abrv}')
            for series in series_list:
               series_ids.append(series['seriesID'])
    
    # Fetch series
    for i in range(0, len(series_ids), 50):
        ids_for_req = series_ids[i:min(len(series_ids), i + 50)]
        body = {
            "seriesid": ids_for_req,
            "startyear": 2005,
            "endyear": 2025,
            "catalog": True,
            "calculations": True,
            "annualaverage": True,
            "aspects": True,
            "registrationkey": BLS_API_KEY
        }
        series_res_url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/'
        res = requests.post(series_res_url, json=body)
        series_data_all = res.json()['Results']['series']
        for series_data in series_data_all:
            series_id = series_data['seriesID']
            
            series_catalog = series_data['catalog']
            series_title = series_catalog['series_title'].replace('\'', '')
            series_survey_name = series_catalog['survey_name'].replace('\'', '')
            series_survey_abbreviation = series_catalog['survey_abbreviation']
            series_measure_data_type = series_catalog['measure_data_type'].replace('\'', '')
        
            series_query = f'INSERT OR REPLACE INTO BLSTimeSeries (SeriesID, Title, SurveyName, SurveyAbbreviation, MeasureDataType) VALUES (\'{series_id}\', \'{series_title}\', \'{series_survey_name}\', \'{series_survey_abbreviation}\', \'{series_measure_data_type}\');'
            print(series_query)
            cursor.execute(series_query)
            sql_connection.commit()

            data_by_period = series_data['data']
            query = 'INSERT INTO TimeSeriesEntry (Year, TimeSeriesID, Period, PeriodName, Value) VALUES \n'
            for i, data_for_period in enumerate(data_by_period):
                year = int(data_for_period['year'])
                period = data_for_period['period']
                period_name = data_for_period['periodName']
                value = float(data_for_period['value'])
                last_char = '\n' if i == len(data_by_period) - 1 else ',\n'
                query += f'({year}, \'{series_id}\', \'{period}\', \'{period_name}\', {value}){last_char}'
            query += ';'
            cursor.execute(query)
            sql_connection.commit()
            fetch_cursor.execute(f'INSERT INTO FetchRecords(Source, Destination, NewRecordsAdded, OperationRan) VALUES (\'BLS Time Series - {series_title}\', \'BLS Database\', \'{len(data_by_period)}\', \'{datetime.datetime.now()}\');')
            fetch_connection.commit()

