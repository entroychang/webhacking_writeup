# old-54_100

* 這一題一進去就看到一個斗大的 the password is 然後快速地晃過很多字
* 這立刻就傳來了一股濃濃的 js 味
* 所以我直接看了原始碼中的 js 並且稍做修改，就拿到 flag 了
    ```js=
    function run(){
  if(window.ActiveXObject){
   try {
    return new ActiveXObject('Msxml2.XMLHTTP');
   } catch (e) {
    try {
     return new ActiveXObject('Microsoft.XMLHTTP');
    } catch (e) {
     return null;
    }
   }
  }else if(window.XMLHttpRequest){
   return new XMLHttpRequest();
 
  }else{
   return null;
  }
     }
    x=run();
    let flag="";
    function answer(i){
      x.open('GET','?m='+i,false);
      x.send(null);
      aview.innerHTML=x.responseText;
      i++;
      if(x.responseText) {
           setTimeout("answer("+i+")",20);
           flag = flag + x.responseText;
           console.log(flag);
      }
      if(x.responseText=="") aview.innerHTML="?";
    }
    setTimeout("answer(0)",1000);
    ```
* flag : FLAG{a7981201c48d0ece288afd01ca43c55b}
