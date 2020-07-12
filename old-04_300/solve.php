<?php
    for ($i = 10000000; $i <= 99999999; $i ++) {
        $hash = $i."salt_for_you";
        $answer = $hash;
        for($j = 0; $j < 500; $j ++)
            $hash = sha1($hash);
        if ($hash == "b7a02b4aa8ce74c54d9c686d0f1d93b065ce69bb") {
            echo $answer;
            break;
        }
    }
?>