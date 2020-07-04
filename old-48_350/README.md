# old-48_350

* 一進到這一個網站，可以看到可以 upload file
* 然後我往這個方向一直想很久，但是是不對的
* 因此，我打開了 burp 思考一下有什麼東東是我漏掉的
* 我嘗試改了 content-type 但是沒什麼用
* 在試過滿久之後，發現了一個小東西有可能可以被利用，那就是 delete file 的時候
* 理論上 delete file 會用到 rm
* 所以說如果我可以加上一些 command injection 來查看資料的話，或許不失為一種辦法
* 用 burp 修改 filename 成 `whatever_you_like; ls` 或是 `whatever_you_like || ls` 都可以
* 之後刷新一下頁面 delete 一下，就可以拿到 flag 了
* flag : FLAG{i_think_this_chall_is_cool}
