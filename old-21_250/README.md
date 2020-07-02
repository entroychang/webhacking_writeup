# old-21_250

* 一進到這一個網站，可以看到大大的提示 --- blind sql injection
* 看到 blind sql injection 十之八九要寫 code 拉
* 現在，要先嘗試一下哪裡是注入點
* 當我輸入 id : guest, pw : guest 的時候，顯示 login success
* 當我輸入 id : guest' # , pw : guest 的時候，顯示 login success
* 當我輸入 id : guest, pw : guest : guest' # 的時候，顯示 wrong password
* 當我輸入 id : guest, pw : 123 的時候，顯示 login fail
* 這告訴我們一個小道理，注入點在 id 
* 所以說我嘗試了一個 payload id : guest' and length(pw)>0 # , pw : guest，顯示 login success
* 現在，只需要寫 code 把 admin 的 password dump 出來就好拉
* 我用的 payload 是 `'or ascii(substr(pw,{},1))={}%23`
* {} 用 code 做替換
* 也可以用 `admin' or pw like '{}%` 來實作
* 如果不知道上面的 payload 在幹嘛，可能要 google 一下
* 據我的猜測，sql 的語句應該是 `select * from table_name where id=''`
* 這樣的話應該比較好明白
* 最後得到的結果會是 `ghere_is_no_rest_for_the_white_angel`
* 很奇怪吧 ... 我是這麼覺得拉，因為應該是 there 才對 ...
* 我也不知道為什麼
* 所以改成 `there_is_no_rest_for_the_white_angel`
* id : admin, pw : there_is_no_rest_for_the_white_angel
* 就過拉
