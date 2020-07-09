<?php
    for ($i = 0; $i < 999999999; $i ++) {
        if (strstr(md5($i, true), "'='")) {
            echo $i . "    is    " . md5($i, true);
            break;
        }
    }
?>