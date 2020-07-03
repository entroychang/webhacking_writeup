# old-39_100

* 這一題一進去就直接看一下 source code 
    ```php=
    $db = dbconnect();
     if($_POST['id']){
        $_POST['id'] = str_replace("\\","",$_POST['id']);
        $_POST['id'] = str_replace("'","''",$_POST['id']);
        $_POST['id'] = substr($_POST['id'],0,15);
        $result = mysqli_fetch_array(mysqli_query($db,"select 1 from member where length(id)<14 and id='{$_POST['id']}"));
        if($result[0] == 1){
          solve(39);
        }
     }
    ```
* 坦白講，這一題我想滿久的，讓我感覺它不只 100 分 = =
* 後來看了一下別人的 write up 才驚醒，對誒 ... 可以加空白
* 什麼意思呢？在 mysql 裡面，`'1' = '1 '` 所以可以加空白壓縮一下字數，最後加一個 '
* 所以語句就變成 `select 1 from member where length(id)<14 and id='1(13個空白)'`
* 因為已經 select 1 了，所以只要後面的語法對，就可以過了
