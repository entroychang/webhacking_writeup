# old-43_250

* 這一題一進去就可以看到提示 You must upload webshell and cat /flag
* 很友善吧 ～～～ 所以我就沒有多想，上傳了一個 php file 內涵 `<?php echo shell_exec("cat /flag") ?>;`
* 然後噴出一個 wrong type
* 誒？ wrong type??? 表示一件大事啊！！！
* 讓我們打開一下 burp 然後上傳一樣的 file，可以看到 `Content-Type: text/php`
* 如果我們把它改成除了 text/php 以外的 type 說不定就可以過了
* 這一題我把它改成 `image/jpg` 送出之後，可以看到吐出了 ./upload/your_filename
* 訪問之後，就可以看到 flag 拉
* flag : FLAG{V2hhdCBkaWQgeW91IGV4cGVjdD8=} 
