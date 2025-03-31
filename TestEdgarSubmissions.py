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

for i in range(1, 50):
    if i % 9 == 0:
        time.sleep(1)
    num_raw = str(i)
    num = num_raw.rjust(3, '0')
    url = f'https://data.sec.gov/submissions/CIK0001557156-submissions-{num}.json'
    print(url)
    r = requests.get(url, headers = HEADERS)
    if r.text.find('0001752724-19-190607') != -1:
        print(i)