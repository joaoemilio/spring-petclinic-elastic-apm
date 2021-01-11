<?php

if (strcasecmp($_SERVER['REQUEST_METHOD'], 'POST') != 0){
    throw new Exception('Expected request method: POST');
}

$contentType = isset($_SERVER["CONTENT_TYPE"]) ? trim($_SERVER["CONTENT_TYPE"]) : '';
if (strcasecmp($contentType, 'application/json') != 0){
    throw new Exception('Expected content type: application/json');
}

$body = file_get_contents("php://input");
$decoded = json_decode($body, true);

if (!is_array($decoded)){
    throw new Exception('Invalid JSON!');
}

$response = array(
	"message" => 'Hello '. $decoded['name'],
);

print_r(json_encode($response));
?>