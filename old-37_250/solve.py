import requests
import os
import time

url = 'https://webhacking.kr/challenge/web-18/index.php'

file_name = 'tmp-{}'.format(str(round(time.time())))
print(file_name)

new_file = open(file_name, 'w+')
new_file.write('')

requests.post(url, files={'upfile': new_file})

os.system('rm -rf {}'.format(file_name))