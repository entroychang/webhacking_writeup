# old-06_100

* 點進去這一個網站的時候，可以看到 view-source, ID, PW，顯而易見的，直接點進去 source code，可以看到以下的畫面
    ```php=
    <?php
    include "../../config.php";
    if($_GET['view_source']) view_source();
    if(!$_COOKIE['user']){
      $val_id="guest";
      $val_pw="123qwe";
      for($i=0;$i<20;$i++){
        $val_id=base64_encode($val_id);
        $val_pw=base64_encode($val_pw);
      }
      $val_id=str_replace("1","!",$val_id);
      $val_id=str_replace("2","@",$val_id);
      $val_id=str_replace("3","$",$val_id);
      $val_id=str_replace("4","^",$val_id);
      $val_id=str_replace("5","&",$val_id);
      $val_id=str_replace("6","*",$val_id);
      $val_id=str_replace("7","(",$val_id);
      $val_id=str_replace("8",")",$val_id);

      $val_pw=str_replace("1","!",$val_pw);
      $val_pw=str_replace("2","@",$val_pw);
      $val_pw=str_replace("3","$",$val_pw);
      $val_pw=str_replace("4","^",$val_pw);
      $val_pw=str_replace("5","&",$val_pw);
      $val_pw=str_replace("6","*",$val_pw);
      $val_pw=str_replace("7","(",$val_pw);
      $val_pw=str_replace("8",")",$val_pw);

      Setcookie("user",$val_id,time()+86400,"/challenge/web-06/");
      Setcookie("password",$val_pw,time()+86400,"/challenge/web-06/");
      echo("<meta http-equiv=refresh content=0>");
      exit;
    }
    ?>
    <html>
    <head>
    <title>Challenge 6</title>
    <style type="text/css">
    body { background:black; color:white; font-size:10pt; }
    </style>
    </head>
    <body>
    <?php
    $decode_id=$_COOKIE['user'];
    $decode_pw=$_COOKIE['password'];

    $decode_id=str_replace("!","1",$decode_id);
    $decode_id=str_replace("@","2",$decode_id);
    $decode_id=str_replace("$","3",$decode_id);
    $decode_id=str_replace("^","4",$decode_id);
    $decode_id=str_replace("&","5",$decode_id);
    $decode_id=str_replace("*","6",$decode_id);
    $decode_id=str_replace("(","7",$decode_id);
    $decode_id=str_replace(")","8",$decode_id);

    $decode_pw=str_replace("!","1",$decode_pw);
    $decode_pw=str_replace("@","2",$decode_pw);
    $decode_pw=str_replace("$","3",$decode_pw);
    $decode_pw=str_replace("^","4",$decode_pw);
    $decode_pw=str_replace("&","5",$decode_pw);
    $decode_pw=str_replace("*","6",$decode_pw);
    $decode_pw=str_replace("(","7",$decode_pw);
    $decode_pw=str_replace(")","8",$decode_pw);

    for($i=0;$i<20;$i++){
      $decode_id=base64_decode($decode_id);
      $decode_pw=base64_decode($decode_pw);
    }

    echo("<hr><a href=./?view_source=1 style=color:yellow;>view-source</a><br><br>");
    echo("ID : $decode_id<br>PW : $decode_pw<hr>");

    if($decode_id=="admin" && $decode_pw=="nimda"){
      solve(6);
    }
    ?>
    </body>
    </html>
    ```
* 這個程式碼的大意就是說，把 val_id 跟 val_pw 先 base64 encode 20 次之後，把 1, 2, 3, 4, 5, 6, 7, 8 全部代換成 !, @, $, ^, &, *, (, )
* 然後新增兩個 cookies user 跟 password，把處理過的資訊塞進去
* decode 的方法就是 encode 的方法反過來做
* 看到最下面，如果 decode 出來的 user = admin, password = nimda，就可以觸發 solve function
* 這一題需要寫 code 幫助解題，在這裡我用的是 python
    * 需要注意的一點是，code 裡面的 PHPSESSID 要用自己的
* 送出去之後就解完拉
    * ![](https://i.imgur.com/ltiUMrT.png)
