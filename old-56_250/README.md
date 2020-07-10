# old-56_250

* 這一題一進去可以發現基本上沒什麼提示，唯一的提示就是主畫面的 sql 標誌了，所以應該是考 sql injection 拉
* 個把 readme 跟 hi~ 點進去可以發現有一個 param 是 read，嘗試一下簡單的 sql injection 可以發現那不是注入點
* 所以就把目光轉向 search 上，從 a 開始，這時發現 guest 不見了，猜想應該是 admin 中 access denied 的內容
* 為了驗證我的想法，輸入了 `hello~` 可以發現只有 guest 出現，這表示 a 是 admin 的內容
* 所以說這一題不太像 sql injection 反而像是考腦筋急轉彎 ... 是說絕大多數的 ctf 都需要通靈之術拉 ...
* 在這裡我用 python 輔助我
* 題個外話，如果直接用我的 script 跑的話會發現結果是 `ag{himiko_toga_is_cute_dont_you_think_so?}`
* 很明顯是 `flag{himiko_toga_is_cute_dont_you_think_so?}` 所以可以直接在 search 那裡先行加上 `flag{` 會比較好看
