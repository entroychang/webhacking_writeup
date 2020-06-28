# old-03_350

* 這一題一點進去就看到一個奇怪的東東
    ![](https://i.imgur.com/nfAFRmL.png)
* 乍看之下，一點頭緒都沒有，亂點一通，可以看到點到的地方變成黑的，送出去跟我說 no
* 看了一下 js 的部分
    ```js=
    function go(){
      var answer="";
      for(i=1;i<=25;i++) { answer=answer+eval("kk._"+i+".value"); }
      kk._answer.value=answer;
      kk.submit();
    }
    ```
    簡單來說，會送出 0101 之類的資料，有一個問題是我不知道到底是怎麼判斷的，只能通靈一下了
* 端詳著這張圖許久，我發現他跟數獨有點像，所以嘗試著滿足每行每列給的數字
    ![](https://i.imgur.com/1ATVMIv.png)
* 過了之後，可以看到
    ![](https://i.imgur.com/7y08GCJ.png)
    隨便輸入個 admin
    ![](https://i.imgur.com/qBQsqBf.png)
* 因為這一題考的是 sql injection，所以我嘗試輸入 'or 1=1 #
    ![](https://i.imgur.com/CNQCmrv.png)
    顯然沒有屁用
* 之後看了一下原始碼，可以看到
    ```
    <input type=hidden name=answer value=1010100000011100101011111>
    ```
    所以我就把 value 改成 1010100000011100101011111' or 1=1 -- 
    ![](https://i.imgur.com/w7UkUPg.png)
    ![](https://i.imgur.com/zafnFbk.png)
    就過拉
