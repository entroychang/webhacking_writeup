# old-38_100

* 這題一進去就有一個斗大的標題 log injection
* 坦白說我也不知道是什麼意思
* 所以我看了一下原始碼，發現有一個隱藏的路徑是 admin.php
* 訪問了之後，給了一個小提示：you have to login as admin
* 所以我回到原本的頁面嘗試 admin 的登陸，看到 you are not admin
* 嘗試了一下 guest，訪問 admin.php，可以看到 your_ip_address:guest
* 誒～～～有沒有很清楚～～～，這一題要考的是 SSRF 拉
* 所以拉，我打開了 burp，在 id=guest 後面加上 %0a%0dadmin 之後，訪問 admin.php 就過拉
