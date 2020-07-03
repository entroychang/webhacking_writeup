# old-41_250

* 進到這一個網站，可以看到 upload file 的部分以及 source code 
    ```php=
    if(isset($_FILES['up']) && $_FILES['up']){
        $fn = $_FILES['up']['name'];
        $fn = str_replace(".","",$fn);
        $fn = str_replace("<","",$fn);
        $fn = str_replace(">","",$fn);
        $fn = str_replace("/","",$fn);

        $cp = $_FILES['up']['tmp_name'];
        copy($cp,"./{$upload_dir}/{$fn}");
        $f = @fopen("./{$upload_dir}/{$fn}","w");
        @fwrite($f,$flag);
        @fclose($f);
        echo("Done~");
      }
    ```
    可以看到除了 copy 以外其他 file 處理的部分，都有神奇的 @，也就是說強致執行的部分
* 所以目標就是要拿到報錯的資訊
* 所以一開始的時候，直接按了 upload 得到了 
    ```
    copy(): Filename cannot be empty in /var/www/html/challenge/web-19/index.php on line 21
    ```
* 再看一下 source code 可以發現我們要找的 `{$upload_dir}` 並沒有出現
* 所以要再想其他的錯誤
* 這時候我就想到，在 linux 系統中，有限制 filename 最大的長度，可以參考一下這一篇[文章](https://unix.stackexchange.com/questions/32795/what-is-the-maximum-allowed-filename-and-folder-size-with-ecryptfs)
* 所以直接把 burp 開起來，把 filename 的地方改成超過 255 個字元就可以了，然後就可以知道 `{$upload_dir}` 的值了 4b0e87fef7b5e8ba83894970c9806042e5d6ec9a
* 這一題我不知道是我理解錯誤還是怎麼樣，據我的理解，應該是我上傳一個 file 然後程式打開它，把 flag 輸入進去，然後訪問即可，但是一直找不到 ... QQ
* 所以我就想到了一個萬能的 filename --- flag
* 訪問 https://webhacking.kr/challenge/web-19/4b0e87fef7b5e8ba83894970c9806042e5d6ec9a/flag 並成功的拿到了 flag
* flag : FLAG{error_msg_is_more_userful_than_you_think}
