# old-26_100

* 點進去這個網站的時候，就看到了 source code，二話不說直接點
    ```php=
    <?php
      if(preg_match("/admin/",$_GET['id'])) { echo"no!"; exit(); }
      $_GET['id'] = urldecode($_GET['id']);
      if($_GET['id'] == "admin"){
        solve(26);
      }
    ?>
    ```
* 程式碼的大意就是，如果 id 有 admin 的話會顯示 no，之後會經過 urldecode，如果 id = admin 的話，觸發 solve function
* 乍看之下根本不可能完成的任務，事實上可以透過 urldecode 來做一點文章，如果傳給 id 的值在經過 urldecode 的時候會變成 admin 不就過了
* 這一題，我把 a 經過 urlencode 一下會變成 %61，怎麼 urlencode 呢？很簡單，把 ascii 表中對應的 16 進位前面加個 % 就可以了
* 這裡要注意一下，因為瀏覽器先行完成一次 urldecode，所以我把 % 給先 encode 了，所以最後的網址變成 https://webhacking.kr/challenge/web-11/?id=%2561dmin
* %2561dmin -> %61dmin -> admin
* ![](https://i.imgur.com/lZABDd3.png)
