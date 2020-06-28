# old-05_300

* 一進去這一個網站，可以看到 login 跟 join
* 點擊 join 的時候可以看到 alert 視窗 Access_Denied，看得我是滿臉問號
* 點擊 login 的時候比較正常一點，這時可以看到網址是 https://webhacking.kr/challenge/web-05/mem/login.php 這時我猜想，join 的網址應該會是 https://webhacking.kr/challenge/web-05/mem/join.php
* 訪問之後，又給我噴出 Access_Denied ... = =，看了原始碼之後
    ```js=
    l = 'a';
    ll = 'b';
    lll = 'c';
    llll = 'd';
    lllll = 'e';
    llllll = 'f';
    lllllll = 'g';
    llllllll = 'h';
    lllllllll = 'i';
    llllllllll = 'j';
    lllllllllll = 'k';
    llllllllllll = 'l';
    lllllllllllll = 'm';
    llllllllllllll = 'n';
    lllllllllllllll = 'o';
    llllllllllllllll = 'p';
    lllllllllllllllll = 'q';
    llllllllllllllllll = 'r';
    lllllllllllllllllll = 's';
    llllllllllllllllllll = 't';
    lllllllllllllllllllll = 'u';
    llllllllllllllllllllll = 'v';
    lllllllllllllllllllllll = 'w';
    llllllllllllllllllllllll = 'x';
    lllllllllllllllllllllllll = 'y';
    llllllllllllllllllllllllll = 'z';
    I = '1';
    II = '2';
    III = '3';
    IIII = '4';
    IIIII = '5';
    IIIIII = '6';
    IIIIIII = '7';
    IIIIIIII = '8';
    IIIIIIIII = '9';
    IIIIIIIIII = '0';
    li = '.';
    ii = '<';
    iii = '>';
    lIllIllIllIllIllIllIllIllIllIl = lllllllllllllll + llllllllllll + llll + llllllllllllllllllllllllll + lllllllllllllll + lllllllllllll + ll + lllllllll + lllll;
    lIIIIIIIIIIIIIIIIIIl = llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + lll + lllllllllllllll + lllllllllllllll + lllllllllll + lllllllll + lllll;
    if (eval(lIIIIIIIIIIIIIIIIIIl).indexOf(lIllIllIllIllIllIllIllIllIllIl) == -1) {
        alert('bye');
        throw "stop";
    }
    if (eval(llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + 'U' + 'R' + 'L').indexOf(lllllllllllll + lllllllllllllll + llll + lllll + '=' + I) == -1) {
        alert('access_denied');
        throw "stop";
    } else {
        document.write('<font size=2 color=white>Join</font><p>');
        document.write('.<p>.<p>.<p>.<p>.<p>');
        document.write('<form method=post action=' + llllllllll + lllllllllllllll + lllllllll + llllllllllllll + li + llllllllllllllll + llllllll + llllllllllllllll +
            '>');
        document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name=' + lllllllll + llll + ' maxlength=20></td></tr>');
        document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name=' + llllllllllllllll + lllllllllllllllllllllll + '></td></tr>');
        document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
    }
    ```
    稍微代換一下（人工代換法
    ```js=
    lIllIllIllIllIllIllIllIllIllIl = o + l + d + z + o + m + b + i + e;
    lIIIIIIIIIIIIIIIIIIl = d + o + c + u + m + e + n + t + . + c + o + o + k + i + e;
    // if(eval(document.cookie.indexOf(oldzombie) == -1))
    if (eval(lIIIIIIIIIIIIIIIIIIl).indexOf(lIllIllIllIllIllIllIllIllIllIl) == -1) {
        alert('bye');
        throw "stop";
    }
    if (eval(d + o + c + u + m + e + n + t + . + 'U' + 'R' + 'L').indexOf(m + o + d + e + '=' + 1) == -1) {
        alert('access_denied');
        throw "stop";
    } else {
        document.write('<font size=2 color=white>Join</font><p>');
        document.write('.<p>.<p>.<p>.<p>.<p>');
        document.write('<form method=post action=' + llllllllll + lllllllllllllll + lllllllll + llllllllllllll + li + llllllllllllllll + llllllll + llllllllllllllll +
            '>');
        document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name=' + lllllllll + llll + ' maxlength=20></td></tr>');
        document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name=' + llllllllllllllll + lllllllllllllllllllllll + '></td></tr>');
        document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
    }
    ```
    簡單來說，如果 cookies 中沒有 oldzombie 存在以及訪問的 url 沒有 mode = 1 這一個參數的話都會被擋下來
* 在新增一個 cookie 叫做 oldzombie 值給 1 以及訪問 https://webhacking.kr/challenge/web-05/mem/join.php?mode=1 成功的進到 join 的畫面
* 之後我隨便新增了 id : 123, pass : 123 並且 login，成功的登入了，但是要成為 admin 才能拿到 flag
    ![](https://i.imgur.com/DHxYQ0m.png)
    ![](https://i.imgur.com/M3VlpPd.png)
* 之後我嘗試用 id : admin，但是會顯示該 id 已經被用過了
* 據我的猜想，如果我註冊的是 admin + 空白，或許可以繞過
* 所以我輸入了 id : admin , pass : admin，發現還是跟我說 id 存在了
* 因此我用了 burp suite 來輔助我，把 id=admin&pw=admin 改成 id=admin%09&pw=admin 然後就看到
    ```html=
    <html>
    <title>Challenge 5</title></head><body bgcolor=black><center>
    <font size=2 color=white>sign up as admin	 success
    ```
    可以看到 admin 後面有空白拉
* 隨後到 login 頁面輸入 id : admin, pass : admin，記得要用 burp 攔截一下，之後在 admin 後面加上 %09 -> id=admin%09&pw=admin 送出，就過拉
