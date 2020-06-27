# old-14_100

* 點進去這一個網站的時候，可以看到一個輸入匡，還有一個 check 的按鈕
* 因為這一題有一點提示是 js 的題目，所以二話不說直接右鍵檢查元素，或是 F12 來看一下原始碼，這邊只截取 js 的部分
    ```js=
    function ck(){
      var ul=document.URL;
      ul=ul.indexOf(".kr");
      ul=ul*30;
      if(ul==pw.input_pwd.value) { location.href="?"+ul*pw.input_pwd.value; }
      else { alert("Wrong"); }
    }
    ```
* 這個程式碼的大意就是我輸入的東西如果等於 ul 並且在該 url 後面加上 ?ul 乘上輸入的值就可以過拉
* 稍微在線上的環境跑一下 js
    ```js=
    var ul="https://webhacking.kr/challenge/js-1/";
    ul=ul.indexOf(".kr");
    ul=ul*30;
    console.log(ul);
    ```
    可以發現 ul 的值是 540，在這裡可以再輸入匡中輸入 540，結果沒有跳出 Wrong，可以證明這個數值是對的
* 之後用計算機稍微算一下 \(540 \times 540 = 291600\)
* 訪問一下 https://webhacking.kr/challenge/js-1/?291600 就可以過拉
    ![](https://i.imgur.com/4VTuneT.png)
