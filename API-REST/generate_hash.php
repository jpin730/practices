<?php

$time = time();
echo
    "Time: $time" . PHP_EOL .
    "Hash: " . sha1($argv[1] . $time . 'the secret') . PHP_EOL;
// php generate_hash.php <UID>