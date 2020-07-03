# old-40_500

* 這一題一進去就看到 no, id, pw，根據我的經驗，考的應該是 sql injection
* 現在的問題是，注入點在哪裡
* 這邊建議各位看官可以自己測試一下，會發現題目真的是他媽的機車
* 在試了一陣子之後，得知了注入點在 no 的地方
* 我最先試的 payload 是 `no=(0)||(1=1)`，發現我可以以 guest 登入成功
* 進而思考，題目的語句是什麼
* 據我的猜測，no 應該在最後面，因為我試過 `no=(0)||(1=1)#` 的 payload，但是還是以 guest 成功登入，所以題目的語句應該是 `select id from table_name where id='guest' and pw='guest' and no=no`
* 這應該是為什麼不管我怎麼註解都會是以 guest 登入
* 所以要改變 id 為 admin
* 試過了 `no=(0)||id='admin'` 但是結果會是失敗的
* 在這裡我疑惑了滿久的，因為沒道理沒有過濾 `'` 我的語句會是失效的 
    `select id from table_name where id='guest' and pw='guest' and no=(0)||id='admin'` 可能是因為 url encode 的原因拉
* 後來因為沒有想法，翻著 web sheet，看著各種 payload，突然看到在 mysql 中，可以用 hex 取代字串的輸入。想說死馬當活馬醫，試試看 `no=(0)||id=0x61646d696e` 發現進到了一個新的地方，寫著 admin password
* 因此，可以推測，只要我的 payload 可以指向 admin，那麼便可以導到這一個頁面
* 這一題沒意外的話需要程式的輔助
* 現在，只需要想一個 payload 可以把 pw 給 dump 出來就可以過了。
* 這是我的 payload `(0)||(substr(pw,{},1)={})&id=guest&pw=guest`
* 第一個 {} 是數字
* 第二個 {} 是 ascii 轉 hex 的值
* 如果可以進到 admin 就記錄下來
* 之後 dump 出來的密碼是 lck_admin
* 我輸入在 admin password 裡面發現不對
* 發現 lck_admin 這一個東東怪怪的，說不定 dump 的資料是錯的（是說 lck 是有意義的拉，韓國的 lol ㄎㄎ
* 所以我就用英文字來猜拉，然後我就猜到了 ㄎㄎ `luck_admin`
