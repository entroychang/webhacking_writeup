# old-34_400

* 一進到這一個網站，就直接跳出一個 alert debug me
* 直接看到原始碼，可以看到 js 的部分並且發現看不太懂
* 想到一開始的 alert，所以直接搜尋一下 alert 可以發現這一個 code 
    `alert(b('0x1e', '14cN'))`
* 放在 console 裡面跑一下，可以發現跳出 alert debug me
* 這時，找到該位置可以發現有一個判斷
    ```js=
    if (location[b('0x19', 'iUmC')][b('0x1a', '6]r1')](0x1) == b('0x1b', 'RLUb')) 
    location[b('0x1c', '4c%d')] = b('0x1d', 'llaF');
    else alert(b('0x1e', '14cN'));
    ```
* 把 `location[b('0x1c', '4c%d')]` 丟到 console 裡面跑，可以發現輸出是 
    `https://webhacking.kr/challenge/js-7/"`
* 把 `b('0x1d', 'llaF')` 丟到 console 裡面跑，可以發現輸出是
    `./?Passw0RRdd=1`
* 一切都十分清晰了，直接訪問 https://webhacking.kr/challenge/js-7/?Passw0RRdd=1 就過拉
