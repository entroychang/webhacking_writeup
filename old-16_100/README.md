# old-16_100

* 點進去這一個網站可以看到星號 ... 看起來沒啥用 ...
* 這一題考的是 js，所以一樣檢查一下網頁的原始碼
    ```html=
    ...
    <body bgcolor=black onload=kk(1,1) onkeypress=mv(event.keyCode)>
    ...
    function mv(cd){
      kk(star.style.left-50,star.style.top-50);
      if(cd==100) star.style.left=parseInt(star.style.left+0,10)+50+"px";
      if(cd==97) star.style.left=parseInt(star.style.left+0,10)-50+"px";
      if(cd==119) star.style.top=parseInt(star.style.top+0,10)-50+"px";
      if(cd==115) star.style.top=parseInt(star.style.top+0,10)+50+"px";
      if(cd==124) location.href=String.fromCharCode(cd)+".php"; // do it!
    }
    ```
    在這裡只有節錄比較重要的部分
* 可以看到 onkeypress 表示說時刻的記錄著按下的按鍵，可以隨便按，看到網頁上的星星增加了
* 當按到特別的按鍵時，會有特別的效果，在 function mv 裡面，可以看到有一個註解 do it，想當然要達成他的目標，要按到特別的鍵
* 查一下 [ascii 表](https://zh.wikipedia.org/wiki/ASCII)，可以看到十位數 124 對應的 ascii 碼是 |
* 按下該鍵之後，網址會變成 https://webhacking.kr/challenge/js-3/%7C.php
* 然後就過拉
    ![](https://i.imgur.com/TDavfRT.png)
