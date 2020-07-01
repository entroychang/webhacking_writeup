# old-11_300

* 點進去這個網站看到了 wrong 跟 source code，當然就直接看拉
    ```php=
    <?php
      $pat="/[1-3][a-f]{5}_.*$_SERVER[REMOTE_ADDR].*\tp\ta\ts\ts/";
      if(preg_match($pat,$_GET['val'])){
        solve(11);
      }
      else echo("<h2>Wrong</h2>");
      echo("<br><br>");
    ?>
    ```
* 這一題很明顯是在考正規表達式，如果說不熟呢 ... （像是我，可以藉助網路上的[正規表達式檢查](https://regex101.com/)的東東來幫忙
* 在這裡，就把這東東攤開來講吧
    [1-3] 表示說要符合 1 到 3 的數字，所以我就選擇了 1
    [a-f] 表示說要符合 a 到 f 的字元，所以我就選擇了 a
    {5} 表示說前面的要符合 5 次，所以說 a -> aaaaa
    _ 表示要有 _
    . 在這裡應該是 php 銜接的地方，所以說我沒有理他
    \* 就是 \* 拉
    $_SERVER[REMOTE_ADDR] 是指自己目前的 ip 位置
    \t 表示 tab，url encode 之後會是 %09
    p 就是要有 p
    a 就是要有 a
    s 就是要有 s
    s 就是要有 s
* 合起來變成 1aaaaa_\*自己的 ip 位置\*%09p%09a%09s%09s
* 就過拉
