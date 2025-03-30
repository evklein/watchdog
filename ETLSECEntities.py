import requests
import os
import sqlite3
import time
from bs4 import BeautifulSoup

EDGAR_DB_CONNECTION_STR = os.path.expanduser(os.environ.get('WATCHDOG_EDGAR_DB_LOC'))
HEADERS = {
    'User-Agent': 'Evan Klein (Indiana University) evklein@iu.edu',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.sec.gov'
}
REQ_LIMIT_PER_SEC = 7 # Timing fun - SEC asks for no more than 10 req/sec.
REQ_LIMIT_PAUSE_INTERVAL = 1.5 # In seconds


def import_filing(sql_connection, cik, filing_id):
    print(f'Scraping NPORT-P Filing {filing_id} for CIK {cik}.')
    req_url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{filing_id}/primary_doc.xml'
    nport_req = requests.get(req_url, headers = HEADERS)
    nport_xml = BeautifulSoup(nport_req.text, 'xml')

    general_info = nport_xml.find('genInfo')
    holdings = nport_xml.find_all('invstOrSec')
    
    # Save series details, if none exists
    save_series_query = f'''
REPLACE INTO SeriesClasses VALUES
(
    {nport_xml.find('seriesId').string}-{nport_xml.find('classId').string},
    {nport_xml.find('seriesId').string},
    {nport_xml.find('classId').string},
    {nport_xml.find('seriesName').string}
);'''
    print(save_series_query)
    cursor.execute(save_series_query)
    sql_connection.commit()

    # Save filing details

    # Save holding details

def pause_comply(nth):
    if nth % REQ_LIMIT_PER_SEC == 0:
        time.sleep(REQ_LIMIT_PAUSE_INTERVAL)

## Make database connections
sql_connection = sqlite3.connect(EDGAR_DB_CONNECTION_STR)
cursor = sql_connection.cursor()

## Get CIKs from database
retrieve_cik_command = 'SELECT CIK FROM SECEntities'
cursor.execute(retrieve_cik_command)
ciks_raw = cursor.fetchall()
ciks = [cik_obj[0] for cik_obj in ciks_raw]

## Grab JSON from EDGAR - pull out what we need an insert it into table
for i, cik in enumerate(ciks):
    ### Grab and store entity details
    req_url = f'https://data.sec.gov/submissions/CIK{cik}.json'
    edgar_req = requests.get(req_url, headers = HEADERS)
    edgar_res = edgar_req.json()
    update_entity_row_command = f'''
UPDATE SECEntities SET
    Name = '{edgar_res["name"]}',
    EntityType = '{edgar_res["entityType"]}',
    IncorporationState = '{edgar_res["stateOfIncorporation"]}',
    PhoneNumber = '{edgar_res["phone"]}',
    Address = '{edgar_res["addresses"]["business"]["street1"]}'
WHERE CIK = '{cik}';
    '''
    cursor.execute(update_entity_row_command)
    sql_connection.commit()

    # Compile filing IDs
    recent_filings = edgar_res['filings']['recent']
    nport_filing_ids = [
        filing[0].replace('-', '')
        for _, filing in enumerate(
            zip(recent_filings['accessionNumber'], recent_filings['form'])
        ) if filing[1] == 'NPORT-P'
    ]

    print(f'{len(nport_filing_ids)} NPORT-P filings found, initiating per-filing scrape(s).')
    for j, filing_id in enumerate(nport_filing_ids):
        import_filing(sql_connection, cik, filing_id)
        pause_comply(j)

    pause_comply(i)
