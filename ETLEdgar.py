import requests
import os
import sqlite3
import time
from bs4 import BeautifulSoup
import datetime

EDGAR_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_EDGAR_DB_LOC'))
FETCH_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_FETCH_DB_LOC'))
HEADERS = {
    'User-Agent': 'Evan Klein (Indiana University) evklein@iu.edu',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.sec.gov'
}
REQ_LIMIT_PER_SEC = 9 # Timing fun - SEC asks for no more than 10 req/sec.
REQ_LIMIT_PAUSE_INTERVAL = 1 # In seconds

global_request_count = 0
global_request_failures = 0

def Fetch(req_url, json=False):
    global global_request_count
    if global_request_count % REQ_LIMIT_PER_SEC == 0:
        time.sleep(REQ_LIMIT_PAUSE_INTERVAL)

    global_request_count += 1
    response = requests.get(req_url, headers = HEADERS)
    return response.json() if json == True else response

def ETLEdgarData(sql_connection, cursor, fetch_sql_connection, fetch_cursor):
    global global_request_failures

    ## Get CIKs from database
    retrieve_cik_command = 'SELECT CIK FROM SECEntities;'
    cursor.execute(retrieve_cik_command)
    ciks_raw = cursor.fetchall()
    ciks = [cik_obj[0] for cik_obj in ciks_raw]
    print(f'{len(ciks)} CIK(s) found. Ready to import.')

    ## Grab JSON from EDGAR - pull out what we need an insert it into table
    for cik in ciks:
        try:
            print(f'Scraping entity submissions for CIK {cik}.')
            
            ### Grab and store entity details
            edgar_res = Fetch(f'https://data.sec.gov/submissions/CIK{cik}.json', json=True)
            nport_filing_ids = CompileFilingIds(edgar_res)
            nport_filing_ids += CombRemainingFileIds(edgar_res)

            print(f'CIK{cik}: {len(nport_filing_ids)} NPORT-P filings found, initiating per-filing scrape(s).')
            for filing_id in nport_filing_ids:
                print(f'Importing Filing - {filing_id} for entity {edgar_res["name"]}')
                try:
                    ImportFiling(sql_connection, cursor, fetch_sql_connection, fetch_cursor, cik, filing_id)
                except RuntimeError as error:
                    global_request_failures += 1
                    print(f'Error scraping filing for CIK {cik}. Error count added to.')
                    print(error)

        except RuntimeError as error:
            global_request_failures += 1
            print(f'Error scraping entity submissions for CIK {cik}. Moving to next.')
            print(error)

def CompileFilingIds(edgar_res):
    recent_filings = edgar_res['filings']['recent']
    return [
        filing[0].replace('-', '')
        for _, filing in enumerate(
            zip(recent_filings['accessionNumber'], recent_filings['form'])
        ) if filing[1] == 'NPORT-P'
    ]

def CombRemainingFileIds(edgar_res):
    additional_filing_ids = []
    additional_cik_files = edgar_res['filings']['files']
    for file in additional_cik_files:
        file_res = Fetch(f'https://data.sec.gov/submissions/{file["name"]}', json=True)
        filings = zip(file_res['accessionNumber'], file_res['form'])
        additional_filing_ids += [filing[0].replace('-', '') for filing in filings if filing[1] == 'NPORT-P']
    return additional_filing_ids

def ImportFiling(sql_connection, cursor, fetch_sql_connection, fetch_cursor, cik, filing_id):
    req_url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{filing_id}/primary_doc.xml'
    nport_req = requests.get(req_url, headers = HEADERS)
    nport_xml = BeautifulSoup(nport_req.text, 'xml')

    general_info = nport_xml.find('genInfo')
    holdings = nport_xml.find_all('invstOrSec')
    
    # Save series details, if none exists
    series_composite_key = f'{nport_xml.find("seriesId").string}-{nport_xml.find("classId").string}'
    save_series_query = f'''
        INSERT OR REPLACE INTO SeriesClasses VALUES
        (
            "{series_composite_key}",
            "{nport_xml.find('seriesId').string}",
            "{nport_xml.find('classId').string}",
            "{nport_xml.find('seriesName').string}"
        );'''
    cursor.execute(save_series_query)

    # Save filing details
    save_filing_query = f'''
        INSERT OR REPLACE INTO NPORTFilings VALUES
        (
            "{filing_id}",
            "{cik}",
            "{series_composite_key}",
            "{nport_xml.find('repPdEnd').string}",
            "{nport_xml.find('repPdDate').string}",
            {float(nport_xml.find('totAssets').string)},
            {float(nport_xml.find('totLiabs').string)}
        );'''
    cursor.execute(save_filing_query)
    sql_connection.commit()

    # Save holding details
    holdings = nport_xml.find_all('invstOrSec')
    print(f'Scraping and loading {len(holdings)} holding(s).')
    for holding in holdings:
        save_holding_query = f'''
            INSERT OR REPLACE INTO FundHoldings (LEI, SecurityName, SecurityTitle, Balance, ValueUSD, PercentOfHoldings, AssetCategory, NPORTFilingId)
            VALUES (
                "{holding.find('lei').string}",
                "{holding.find('name').string}",
                "{holding.find('title').string}",
                {float(holding.find('balance').string)},
                {float(holding.find('valUSD').string)},
                {float(holding.find('pctVal').string)},
                "{holding.find('assetCat').string if holding.find('assetCat') is not None else ''}",
                "{filing_id}"
            );'''
        cursor.execute(save_holding_query)
    sql_connection.commit()
    fetch_cursor.execute(f'INSERT INTO FetchRecords (Source, Destination, NewRecordsAdded, OperationRan) VALUES (\'N-PORT for CIK {cik}\', \'Edgar Database\', {len(holdings)}, \'{datetime.datetime.now()}\');')
    fetch_sql_connection.commit()


if __name__ == "__main__":
    ## Make database connections
    sql_connection = sqlite3.connect(EDGAR_DB_CONNECTION_STR)
    cursor = sql_connection.cursor()
    fetch_sql_connection = sqlite3.connect(FETCH_DB_CONNECTION_STR)
    fetch_cursor = fetch_sql_connection.cursor()

    ETLEdgarData(sql_connection, cursor, fetch_sql_connection, fetch_cursor)
    global_request_count = 0
    global_request_failures = 0
    print(f'ETL for Edgar CIKs complete. {global_request_count} requests to EDGAR made. {global_request_failures} failures detected.')

