# old-24_100

* 一進去網頁，直接看 source code 
    ```php=
    <?php
      extract($_SERVER);
      extract($_COOKIE);
      $ip = $REMOTE_ADDR;
      $agent = $HTTP_USER_AGENT;
      if($REMOTE_ADDR){
        $ip = htmlspecialchars($REMOTE_ADDR);
        $ip = str_replace("..",".",$ip);
        $ip = str_replace("12","",$ip);
        $ip = str_replace("7.","",$ip);
        $ip = str_replace("0.","",$ip);
      }
      if($HTTP_USER_AGENT){
        $agent=htmlspecialchars($HTTP_USER_AGENT);
      }
      echo "<table border=1><tr><td>client ip</td><td>{$ip}</td></tr><tr><td>agent</td><td>{$agent}</td></tr></table>";
      if($ip=="127.0.0.1"){
        solve(24);
        exit();
      }
      else{
        echo "<hr><center>Wrong IP!</center>";
      }
    ?>
    ```
* 簡單來說，只要 ip = 127.0.0.1 就可以過了
* 不過要怎麼樣才能動到 `$REMOTE_ADDR` 呢？
* 可以看到一個非常有趣的東東 `extract($_COOKIE);`
* 所以 `$REMOTE_ADDR` = `$_COOKIE[REMOTE_ADDR]`
* 誒～～～ 所以只要新增一個 cookie 叫做 REMOTE_ADDR 就可以改變 ip 的 value 了
* 現在要思考的是要怎麼在一堆 str_replace 之後會變成 127.0.0.1
* 最終會生成 `112277...00...00...1`
* 就過拉
