# old-61_200

* 這一題先看到 source code
    ```php=
    include "../../config.php";
    if($_GET['view_source']) view_source();
    $db = dbconnect();
    if(!$_GET['id']) $_GET['id']="guest";
    echo "<html><head><title>Challenge 61</title></head><body>";
    echo "<a href=./?view_source=1>view-source</a><hr>";
    $_GET['id'] = addslashes($_GET['id']);
    if(preg_match("/\(|\)|select|from|,|by|\./i",$_GET['id'])) exit("Access Denied");
    if(strlen($_GET['id'])>15) exit("Access Denied");
    $result = mysqli_fetch_array(mysqli_query($db,"select {$_GET['id']} from chall61 order by id desc limit 1"));
    echo "<b>{$result['id']}</b><br>";
    if($result['id'] == "admin") solve(61);
    echo "</body></html>";
    ```
* 不難看出只要 id = admin 就可以過了
* 因為過濾的單引號，進而推測要用 `0x0x61646d696e` 當成是 admin
* 直接 select admin as id 就可以了
* `select 0x61646d696e as id` 送出之後發現 access denied，因為字數大於 15 個字
* 在這裡 `as` 可以被省略，所以變成 `select 0x61646d696e id`，送出之後就過了
