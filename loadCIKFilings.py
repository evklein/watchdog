import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Evan Klein (Indiana University) evklein@iu.edu',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.sec.gov/'
}

CIK = '0000906352'
r = requests.get(f'https://data.sec.gov/submissions/CIK{CIK}.json', headers = headers)
data = r.json()
recent_filings = data['filings']['recent']
nport_filing_ids = [
    f[0].replace('-', '')
    for i, f in enumerate(
        zip(recent_filings['accessionNumber'], recent_filings['form'])
    ) if f[1] == 'NPORT-P'
]

for i in range(0, 10):
    req_url = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{nport_filing_ids[i]}/primary_doc.xml'
    nport_req = requests.get(req_url, headers = headers)
    nport_xml = BeautifulSoup(nport_req.text, 'xml')
    
    # Parsing
    general_info = nport_xml.find('genInfo')
    holdings = nport_xml.find_all('invstOrSec')
    print(general_info) 