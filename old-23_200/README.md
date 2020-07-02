# old-23_200

* 一進到這一個網站，就給了赤裸裸的提示 --- Your mission is to inject <script>alert(1);</script>
* 所以目標是 xss
* 直接輸入 <script>alert(1);</script> 可以發現被過濾了
* 在漫長的測試之中，發現了只要有兩個英文字元連在一起就會被過濾
* 所以只要在各字元後面加上某一個東西合起來是 <script>alert(1);</script> 就可以了
* 在漫長的測試過程中發現了是 %00
* 所以 payload 是 <s%00c%00r%00i%00p%00t>a%00l%00e%00r%00t%00(1);</s%00c%00r%00i%00p%00t>
* 注意一件事，上面的 payload 要直接放在 url 裡面，如果放在 box 裡面送出的話，% 會被 url encode
