# old-15_50

* 這一題一點進去，本來以為題目壞掉了 Orz ...，因為直接出現以下畫面
    ![](https://i.imgur.com/3ELJAGI.png)
* 所以我用 postman 來看看這題到底在幹嘛
    ```html=
    <html>

    <head>
        <title>Challenge 15</title>
    </head>

    <body>
        <script>
            alert("Access_Denied");
      location.href='/';
      document.write("<a href=?getFlag>[Get Flag]</a>");
        </script>
    </body>
    ```
    可以清楚地看到啊，一開始就直接 alert，點掉之後啊，直接回到主畫面
* 後面可以看到一個非常可疑的東東 --- ?getFlag，所以我直接訪問 https://webhacking.kr/challenge/js-2/?getFlag 然後就過拉
    ![](https://i.imgur.com/f6Z8ml0.png)
