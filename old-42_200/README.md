# old-42_200

* 這一題可以發現有 test.txt 跟 flag.docx 可以 download 
* 可以順利的 download test.txt 但是 flag.docx 會 alert access denied 
* 這時看了一下原始碼，可以發現一個非常有趣的東東
    ```html=
    <a href="?down=dGVzdC50eHQ=">download</a>
    ```
    down 後面的東東很明顯是 base64 啊
* 所以稍微 decode 一下，可以發現那東東是 text.txt
* 因此可以理所當然地把 flag.docx decode 一下 `ZmxhZy5kb2N4` 之後訪問 https://webhacking.kr/challenge/web-20/?down=ZmxhZy5kb2N4 然後就可以順利的下載拉
