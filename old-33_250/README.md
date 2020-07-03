# old-33_250

* 這一題有 10 個小題，很煩 = = ，要有耐心才行
* 我用 python 輔助，把所有解的過程都記錄在上面了
* 基本上只不過是把 php 換成 python
* 第一題 https://webhacking.kr/challenge/bonus-6/
    * code : 
        ```php=
        if($_GET['get']=="hehe") echo "<a href=???>Next</a>";
        else echo("Wrong");
        ```
    * 很簡單的 get
    * 所以只要在 url 後面加上 ?get=hehe 就可以了
* 第二題 https://webhacking.kr/challenge/bonus-6/lv2.php
    * code : 
        ```php=
        if($_POST['post']=="hehe" && $_POST['post2']=="hehe2") 
        echo "<a href=???>Next</a>";
        else echo "Wrong";
        ```
    * 很簡單的 post
    * 想辦法 post post : hehe, post2 = hehe2 就可以了
* 第三題 https://webhacking.kr/challenge/bonus-6/33.php
    * code : 
        ```php=
        if($_GET['myip'] == $_SERVER['REMOTE_ADDR']) 
        echo "<a href=???>Next</a>";
        else echo "Wrong";
        ```
    * 找到自己的 ip 位置
    * 之後在 url 後面加上 ?myip=your_ip_address 就可以了
* 第四題 https://webhacking.kr/challenge/bonus-6/l4.php
    * code : 
        ```php=
        if($_GET['password'] == md5(time())) 
        echo "<a href=???>Next</a>";
        else echo "hint : ".time();
        ```
    * md5(time()) 之後，在 url 後面加上 ?password=hashed_time 就可以了
* 第五題 https://webhacking.kr/challenge/bonus-6/md555.php
    * code : 
        ```php=
        if($_GET['imget'] && $_POST['impost'] && $_COOKIE['imcookie']) 
        echo "<a href=???>Next</a>";
        else echo "Wrong";
        ```
    * 只要有 get imget = 1, post impost = 1, cookies imcookie = 1，就可以了
* 第六題 https://webhacking.kr/challenge/bonus-6/gpcc.php
    * code : 
        ```php=
        if($_COOKIE['test'] == md5($_SERVER['REMOTE_ADDR']) && $_POST['kk'] == md5($_SERVER['HTTP_USER_AGENT'])) 
        echo "<a href=???>Next</a>";
        else echo "hint : {$_SERVER['HTTP_USER_AGENT']}";
        ```
    * cookies test = md5(your_ip_address), post kk = md5(user_agent)，就可以了
* 第七題 https://webhacking.kr/challenge/bonus-6/wtff.php
    * code : 
        ```php=
        $_SERVER['REMOTE_ADDR'] = str_replace(".","",$_SERVER['REMOTE_ADDR']);
        if($_GET[$_SERVER['REMOTE_ADDR']] == $_SERVER['REMOTE_ADDR']) 
        echo "<a href=???>Next</a>";
        else echo "Wrong<br>".$_GET[$_SERVER['REMOTE_ADDR']];
        ```
    * 把自己的 ip 位置的 . 替換成空，之後把 結果 = 結果，就可以了
* 第八題 https://webhacking.kr/challenge/bonus-6/ipt.php
    * code : 
        ```php=
        extract($_GET);
        if(!$_GET['addr']) 
        $addr = $_SERVER['REMOTE_ADDR'];
        if($addr == "127.0.0.1") 
        echo "<a href=???>Next</a>";
        else echo "Wrong";
        ```
    * 因為有 extract($_GET)，所以 \$addr 可以視為 $_GET['addr']
    * 所以在 url 後面加上 ?addr=127.0.0.1 就可以了
* 第九題 https://webhacking.kr/challenge/bonus-6/nextt.php
    * code : 
        ```php=
        for($i=97;$i<=122;$i=$i+2){
          $answer.=chr($i);
        }
        if($_GET['ans'] == $answer) echo "<a href=???.php>Next</a>";
        else echo "Wrong";
        ```
    * 單純照著 for 跑拿到 answer 之後
    * 在 url 後面加上 ?ans=answer 就可以了
* 第十題 https://webhacking.kr/challenge/bonus-6/forfor.php
    * code : 
        ```php=
        $ip = $_SERVER['REMOTE_ADDR'];
        for($i=0;$i<=strlen($ip);$i++) $ip=str_replace($i,ord($i),$ip);
        $ip=str_replace(".","",$ip);
        $ip=substr($ip,0,10);
        $answer = $ip*2;
        $answer = $ip/2;
        $answer = str_replace(".","",$answer);
        $f=fopen("answerip/{$answer}_{$ip}.php","w");
        fwrite($f,"<?php include \"../../../config.php\"; solve(33); unlink(__FILE__); ?>");
        fclose($f);
        ```
    * 照著題目跑過之後，可以拿到 answer 跟 ip
    * 訪問 https://webhacking.kr/challenge/bonus-6/answerip/answer_ip.php 就可以了
