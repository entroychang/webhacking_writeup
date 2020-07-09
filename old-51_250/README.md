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
* 所以說現在的任務就是要想一下要怎麼樣繞過了，這時，我想到了一個很有趣的東西，在 mysql 中，如果 false = false 那在判定之後會是 true，只要找到某一個直在 hash 之後會有 `'='` 就可以了，在這裡我用了 php 作為輔助
* 可以知道在經過 hash 過後的值是 `�7���ıA@J�'='��%`，直接把它放到整句的語句中看看就可以知道
    ```mysql=
    select id from chall51 where id='admin' and pw='�7���ıA@J�'='��%'
    ```
    可以發現，前面那 `pw='�7���ıA@J�'` 是 false，`'��%'` 是 false，所以就可以繞過拉
