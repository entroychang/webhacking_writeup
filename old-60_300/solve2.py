import requests

url = 'https://webhacking.kr/challenge/web-37/?mode=auth'
cookies = {
    'PHPSESSID' : '2'
}

for _ in range(20):
    response = requests.get(url, cookies=cookies)
    print(response.text)