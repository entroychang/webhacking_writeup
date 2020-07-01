# old-10_250

* 點進去這個網站的時候可以看到一個 O 跟 goal 的長型跑道（？
* 直接查看他的原始碼
    ```html=
    <a id="hackme" style="position:relative;left:0;top:0" onclick="this.style.left=parseInt(this.style.left,10)+1+'px';if(this.style.left=='1600px')this.href='?go='+this.style.left" onmouseover="this.innerHTML='yOu'" onmouseout="this.innerHTML='O'">O</a>
    ```
    這裡我只有節錄比較重要的部分，可以看到當點擊 O 的時候，他會往前進一下
* 這個題目最終的目的就是要到達 goal 的地方，所以可以一直點（？會累死 ... 要點 1600 下歐
* 我直接修改成
    ```html=
    <a id="hackme" style="position:relative;left:0;top:0" onclick="this.style.left=parseInt(this.style.left,10)+1+'px';if(this.style.left=='1600px')this.href='?go='+this.style.left" onmouseover="this.innerHTML='yOu'" onmouseout="this.innerHTML='O'">O</a>
    ```
    之後就直接點擊 O 就過拉
