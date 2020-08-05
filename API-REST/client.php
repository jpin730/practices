<?php

$ch = curl_init($argv[1]); // Client URL handle
curl_setopt(
    $ch, 
    CURLOPT_RETURNTRANSFER,
    true
);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

switch ($httpCode) {
    case 200:
        echo 'OK'.PHP_EOL;
        break;
    case 400:
        echo 'Incorrect request'.PHP_EOL;
        break;
    case 404:
        echo 'Not Found'.PHP_EOL;
        break;
    case 500:
        echo 'Server fell'.PHP_EOL;
        break;
    default:
        echo 'Undefined'.PHP_EOL;
        break;
}