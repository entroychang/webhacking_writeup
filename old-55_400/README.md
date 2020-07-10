# old-55_400

* 這一題一進去就可以看到一個遊戲，還有一個 rank 的頁面
* 點進去之後，發現下面有提示 `mysqli_query($db,"insert into chall55 values('{$_SESSION['id']}','".trim($_POST['score'])."','{$flag}')");`
* 這應該是指分數是怎麼新增的
* 所以用膝蓋想這一題一定是考 sql injection 以及注入點就在 score 那邊
* 現在的任務就是找到 colume name 來把資料 dump 下來
* 有過濾一些關鍵的字，像是 select 就不能用，所以沒辦法用 union select 了
* 還有一個東東可以用就是 procedure analyse()
* `?score=2147483647%20procedure%20analyse()` 可以看到 `id : webhacking.chall55.id` 表示 table name 是 chall55 以及其中一個 colume name id
* 那要怎麼找其他的 colume name 呢？這時就需要用到 limit 拉
* `?score=2147483647%20limit%201,1%20procedure%20analyse()`
    `webhacking.chall55.score`
    `?score=2147483647%20limit%202,1%20procedure%20analyse()`
    `webhacking.chall55.p4ssw0rd_1123581321`
    誒 ～～～ 可以發現有一個非常像是需要被 dump 資料的一個 colume 出現了
* 知道了 colume name 就可以開始上工拉
* 不過在上工之前，要先確認一下這是什麼類型的 sql injectio，稍微測試一下 `?score=0||1=1` `her0gyu // 57` 可以發現只要語句是對的但是沒有明確的指定成績的話會輸出的人名以及成績
* 然後就可以正式上工了，要注意的是有過濾一些關鍵字，所以我的 payload 也是試了很長一段時間的 ...
* 基本上我用的是 `or p4ssw0rd_1123581321 like '{}%'` 的語句，再稍加變化而已
