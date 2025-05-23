import requests
import time

HEADERS = {
    'User-Agent': 'Evan Klein (Indiana University) evklein@iu.edu',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.sec.gov'
}

# ('0000906352'),
# ('0000886982'),
# ('0001557156'),
# ('0000102909'),
# ('0001920453'),
# ('0001331875'),
# ('0000036405')


url = f'https://data.sec.gov/submissions/CIK0000906352.json'

r = requests.get(url, headers = HEADERS)
data = r.json()
recent_filings = data['filings']['recent']
filings_with_type = zip(recent_filings['accessionNumber'], recent_filings['form'])
nq = [filing for filing in filings_with_type if filing[1] == 'NPORT-P']
print(nq)