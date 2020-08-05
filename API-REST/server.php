<?php

// HTTP AUTH
/* $user = array_key_exists('PHP_AUTH_USER', $_SERVER) ? $_SERVER['PHP_AUTH_USER'] : '';
$password = array_key_exists('PHP_AUTH_PW', $_SERVER) ? $_SERVER['PHP_AUTH_PW'] : '';
if ($user !== 'jaime' || $password !== '1234') {
    die;
} */


// HMAC AUTH
/* if (
    !array_key_exists('HTTP_X_HASH', $_SERVER) ||
    !array_key_exists('HTTP_X_TIMESTAMP', $_SERVER) ||
    !array_key_exists('HTTP_X_UID', $_SERVER)
    ) {
        die;
    }
    list($hash, $uid, $timestamp) = [
        $_SERVER['HTTP_X_HASH'],
        $_SERVER['HTTP_X_UID'],
        $_SERVER['HTTP_X_TIMESTAMP']
];
$secret = 'the secret';
$newHash = sha1($uid . $timestamp . $secret);
if ($newHash !== $hash) {
    die;
} */

// ACCESS TOKEN AUTH
/* if ( !array_key_exists('HTTP_X_TOKEN', $_SERVER) ) {
    die;
}
$url = 'http://localhost:8001';
$ch = curl_init($url); // Client URL handle
curl_setopt(
    $ch,
    CURLOPT_HTTPHEADER,
    ["X-Token: {$_SERVER['HTTP_X_TOKEN']}"]
);
curl_setopt(
    $ch, 
    CURLOPT_RETURNTRANSFER,
    true
);
$ret = curl_exec($ch);
if ($ret !== 'true') {
    die;
} */

// Define allowed resources
$allowedResourceTypes = [
    'books',
    'authors',
    'genres'
];

// Get resource type
$resourcesType = $_GET['resource_type'];
// Validate resource availability
if ( !in_array($resourcesType, $allowedResourceTypes) ) {
    http_response_code(400);
    die;
}

// Define resources
$books = [
    1 => [
        'title' => 'Title 1',
        'id_author' => 1,
        'id_genre' => 1
    ],
    2 => [
        'title' => 'Title 2',
        'id_author' => 2,
        'id_genre' => 2
    ],
    3 => [
        'title' => 'Title 3',
        'id_author' => 3,
        'id_genre' => 3
        ]
    ];
    
    // Create resource ID
    $resourcesId = array_key_exists('resource_id', $_GET) ? $_GET['resource_id'] : '';
    
    header('Content-Type: application/json');
    
    // Generate response
    switch ( strtoupper($_SERVER['REQUEST_METHOD']) ) {
    case 'GET':
        if ( empty($resourcesId) ) {
            echo json_encode($books);
        }
        else {
            if ( array_key_exists($resourcesId, $books) ) {
                echo json_encode($books[$resourcesId]);
            }
            else {
                http_response_code(404);
            }
        }
        break;
        case 'POST':
            $json = file_get_contents('php://input'); // raw POST
            $books[] = json_decode($json, true); // true means return array type
        // echo array_keys($books)[count($books) - 1];
        echo json_encode($books);
        break;
    case 'PUT':
        // Validate resource already exists
        if ( !empty($resourcesId) && array_key_exists( $resourcesId, $books) ) {
            $json = file_get_contents('php://input');
            $books[$resourcesId] = json_decode($json, true); // item complete replacement
            echo json_encode($books);
        }
        break;
    case 'DELETE':
        if ( !empty($resourcesId) && array_key_exists( $resourcesId, $books) ) {
            unset($books[$resourcesId]);
            echo json_encode($books);
        }
        break;
}