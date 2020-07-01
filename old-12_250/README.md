# old-12_250

* 一進入網站，就明著說是考 javascript 了，所以直接把 script 的部分攤開來看，可以看到 
ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀ ...
* 這是一種 encode 的手法，叫做 aaencode，可以用 [aadecode](https://cat-in-136.github.io/2010/12/aadecode-decode-encoded-as-aaencode.html) 來解密一下
    ```js=
    var enco='';
    var enco2=126;
    var enco3=33;
    var ck=document.URL.substr(document.URL.indexOf('='));
    for(i=1;i<122;i++){
      enco=enco+String.fromCharCode(i,0);
    }
    function enco_(x){
      return enco.charCodeAt(x);
    }
    if(ck=="="+String.fromCharCode(enco_(240))+String.fromCharCode(enco_(220))+String.fromCharCode(enco_(232))+String.fromCharCode(enco_(192))+String.fromCharCode(enco_(226))+String.fromCharCode(enco_(200))+String.fromCharCode(enco_(204))+String.fromCharCode(enco_(222-2))+String.fromCharCode(enco_(198))+"~~~~~~"+String.fromCharCode(enco2)+String.fromCharCode(enco3)){
      location.href="./"+ck.replace("=","")+".php";
    }
    ```
* 之後分析一下這個 code 可以發現 ck 滿足某一個條件的時候可以訪問另一個頁面
* 把 `String.fromCharCode(enco_(240))+String.fromCharCode(enco_(220))+String.fromCharCode(enco_(232))+String.fromCharCode(enco_(192))+String.fromCharCode(enco_(226))+String.fromCharCode(enco_(200))+String.fromCharCode(enco_(204))+String.fromCharCode(enco_(222-2))+String.fromCharCode(enco_(198))+"~~~~~~"+String.fromCharCode(enco2)+String.fromCharCode(enco3)` 用 js 跑一下可以發現輸出是 youaregod~~~~~~~! 
* 所以訪問 youaregod~~~~~~~!.php 之後，就過拉
