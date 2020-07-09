# old-51_250

* 這一題一進去就聞到了一股濃濃的 sql injection 的味道
* 直接看一下 source code
    ```php=
    if($_POST['id'] && $_POST['pw']){
        $db = dbconnect();
        $input_id = addslashes($_POST['id']);
        $input_pw = md5($_POST['pw'],true);
        $result = mysqli_fetch_array(mysqli_query($db,"select id from chall51 where id='{$input_id}' and pw='{$input_pw}'"));
        if($result['id']) solve(51);
        if(!$result['id']) echo "<center><font color=green><h1>Wrong</h1></font></center>";
     }
    ```
* 在這裡可以注意到好像沒什麼漏洞啊，因為有 `addslashes` 防止截斷語句
* 有 `md5` 可以加密 ... 誒？ 怎麼會是 true ???
* 在這裡可以參考一下[這篇文章](https://www.w3school.com.cn/php/func_string_md5.asp)，可以知道 true 跟 false 輸出的結果有本質的不同，所以也能因此做些文章拉
* 上網找了一下，可以[參考這一篇](https://blog.werner.wiki/php-md5-true-sqli/)，直接在 pw 那裡輸入 `129581926211651571912466741651878684928` 在 id 輸入 `admin` 就可以過了
