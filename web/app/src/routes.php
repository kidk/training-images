<?php

use Slim\Http\Request;
use Slim\Http\Response;

$app->get('/', function (Request $request, Response $response, array $args) {
    return $this->renderer->render($response, 'index.phtml', ['page' => 'home.phtml', 'args' => []]);
});

$app->get('/submit', function (Request $request, Response $response, array $args) {
    return $this->renderer->render($response, 'index.phtml', ['page' => 'submit.phtml', 'args' => []]);
});

$app->post('/submit/post', function (Request $request, Response $response, array $args) {
    $data = json_encode($request->getParsedBody());

    // Send to receiver
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL,"http://".RECEIVER_HOST.":8080/post");
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Content-Type: application/json',
        'Content-Length: ' . strlen($data))
    );

    // receive server response ...
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $server_output = curl_exec($ch);

    if ($server_output === FALSE) {
        var_dump(curl_error($ch));
        var_dump(curl_errno($ch));
    }

    curl_close ($ch);

    echo $server_output;
});

$app->get('/stats', function (Request $request, Response $response, array $args) {
    return $this->renderer->render($response, 'index.phtml', ['page' => 'stats.phtml', 'args' => []]);
});

$app->get('/stats/ranking', function (Request $request, Response $response, array $args) {
    $data = file_get_contents('http://'.RECEIVER_HOST.':8080/ranking');
    return $response->withJson(json_decode($data));
});

$app->get('/stats/letters', function (Request $request, Response $response, array $args) {
    $data = file_get_contents('http://'.RECEIVER_HOST.':8080/letters');
    return $response->withJson(json_decode($data));
});

$app->get('/search', function (Request $request, Response $response, array $args) {
    return $this->renderer->render($response, 'index.phtml', ['page' => 'search.phtml', 'args' => []]);
});
