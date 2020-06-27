# old-01_200

* 一進到網站內，可以看到一片漆黑，只有 source code 可以按，想當然耳就按下去拉
* 可以看到該網站的源碼
    ```php=
    <?php
  include "../../config.php";
  if($_GET['view-source'] == 1){ view_source(); }
  if(!$_COOKIE['user_lv']){
    SetCookie("user_lv","1",time()+86400*30,"/challenge/web-01/");
    echo("<meta http-equiv=refresh content=0>");
  }
    ?>
    <html>
    <head>
    <title>Challenge 1</title>
    </head>
    <body bgcolor=black>
    <center>
    <br><br><br><br><br>
    <font color=white>
    ---------------------<br>
    <?php
      if(!is_numeric($_COOKIE['user_lv'])) $_COOKIE['user_lv']=1;
      if($_COOKIE['user_lv']>=6) $_COOKIE['user_lv']=1;
      if($_COOKIE['user_lv']>5) solve(1);
      echo "<br>level : {$_COOKIE['user_lv']}";
    ?>
    <br>
    <a href=./?view-source=1>view-source</a>
    </body>
    </html>
    ```
* 簡單來說，這程式碼的大意就是，設定一個 cookie 叫做 user_lv，如果沒有這個 cookie，就設定一個值是 1，如果大於等於 6，把 user_lv 設定成 1，如果 user_lv 大於 5，就可以觸發 solve 這一個 function
* 解題的思路就是，需要一個數字可以滿足上述條件大於 5 不大於 6，所以說在 5 跟 6 之間挑一個數字並且修改 cookie 的值就可以通過拉。我用的數字是 5.5
* 這裡推薦大家可以用一個 google 的插件 [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=zh-TW)，它可以幫助我們輕鬆的修改 cookie 的值或是新增等等。
* 具體的修改方式就是把 1 改成 5.5
    * ![](https://i.imgur.com/hgaDBaB.png)
* 改了之後要記得按綠色的勾勾
    * ![](https://i.imgur.com/JX5wXAt.png)
* 刷新一下網頁之後就過拉
    * ![](https://i.imgur.com/4PghIQs.png)
