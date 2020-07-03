import requests

url = 'https://webhacking.kr/challenge/code-5/?hit=your_id'
cookies = {
    'PHPSESSID' : 'your_phpsessid'
}

for _ in range(1, 100):
    request = requests.get(url, cookies=cookies)
