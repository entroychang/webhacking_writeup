# old-19_150

* 這一題一進去就出現一個 admin submit 的東東，按了之後理所當然地知道我不是 admin = =
* 所以我就輸入了 guest，並且發現可以登錄（？
* 這時 cookies 裡有一個新的東西叫做 userid，又覺得他很像 base64（經驗不要打我，所以稍微 decode 一下
    ```
  b2f5ff47436671b6e533d8dc3614845d7b774effe4a349c6dd82ad4f4f21d34ce1671797c52e15f763380b45e841ec3203c7c0ace395d80182db07ae2c30f034e358efa489f58062f10dd7316b65649e
    ```
    這裡要說一下，後面有奇怪的字元的時候，不要理他
* 這時，覺得一定在哪裡看過，所以我試著把 admin 分開來輸入，得到了以下的結果
    0cc175b9c0f1b6a831c399e269772661 -- a
    MGNjMTc1YjljMGYxYjZhODMxYzM5OWUyNjk3NzI2NjE%3D -- a
    8277e0910d750195b448797616e091ad -- d
    ODI3N2UwOTEwZDc1MDE5NWI0NDg3OTc2MTZlMDkxYWQ%3D -- d
    ...
* 誒～～～這很明顯就是 md5 雜湊啊，看起來（經驗不要打我，所以我就 decrypt 了一下，可以發現就是如此。那麼邏輯就十分的清晰了，cookie 的內容其實就是 md5(a) + md5(d) + ... + md5(n) 再經過 base64 encode 過後的值
* 所以 md5(a) + md5(d) + ... + md5(n)
    ```
  0cc175b9c0f1b6a831c399e2697726618277e0910d750195b448797616e091ad6f8f57715090da2632453988d9a1501b865c0c0b4ab0e063e5caa3387c1a87417b8b965ad4bca0e41ab51de7b31363a1
    ```
    base64 encode 之後
    ```
  MGNjMTc1YjljMGYxYjZhODMxYzM5OWUyNjk3NzI2NjE4Mjc3ZTA5MTBkNzUwMTk1YjQ0ODc5NzYxNmUwOTFhZDZmOGY1NzcxNTA5MGRhMjYzMjQ1Mzk4OGQ5YTE1MDFiODY1YzBjMGI0YWIwZTA2M2U1Y2FhMzM4N2MxYTg3NDE3YjhiOTY1YWQ0YmNhMGU0MWFiNTFkZTdiMzEzNjNhMQ==
    ```
    之後把 userid 改掉就過拉

