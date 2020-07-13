# old-57_600

* 直接看到 source code 
    ```php=
    $db = dbconnect();
  if($_GET['msg'] && isset($_GET['se'])){
        $_GET['msg'] = addslashes($_GET['msg']);
        $_GET['se'] = addslashes($_GET['se']);
        if(preg_match("/select|and|or|not|&|\||benchmark/i",$_GET['se'])) exit("Access Denied");
        mysqli_query($db,"insert into chall57(id,msg,pw,op) values('{$_SESSION['id']}','{$_GET['msg']}','{$flag}',{$_GET['se']})");
        echo "Done<br><br>";
        if(rand(0,100) == 1) mysqli_query($db,"delete from chall57");
  }
    ```
* 乍看之下，似乎拿不到什麼資料，只有不停的 insert 資料而已
* 所以我們要製造可以判斷的情況，就要依靠 time based blind sql injectiono 來實現
* 可以先用 `?msg=123&se=if(length(pw)>0,sleep(3),1)=1` 來驗證一下，可以發現過了幾秒才有結果，如果要更精確，可以開啟網頁開發者工具 F12，開啟 network 的部分，可以看到在 time 的位置會大於 3 秒，要記得開道 network 刷新一下頁面才有歐
* 接下來就是 payload 時間，這是我的 payload `if(ascii(substr(pw,{},1))={},sleep(3),1)=1` {} 放變動的值
* 這句話簡單來說就是從 pw 的最左邊開始如果等於某一個值的話，就會延遲 3 秒
* 我是用 python 實現的
* flag : FLAG{y2u.be/kmPgjr0EL64} 
