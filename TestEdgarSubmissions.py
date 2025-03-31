import requests

HEADERS = {
    'User-Agent': 'Evan Klein (Indiana University) evklein@iu.edu',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.sec.gov'
}

for i in range(1, 41):
    num_raw = str(i)
    num = num_raw.rjust(3, '0')
    url = f'https://data.sec.gov/submissions/CIK0000886982-submissions-{num}.json'
    r = requests.get(url, headers = HEADERS)
    print(r.text)
    if r.text.find('NPORT-P') != -1:
        print(i)