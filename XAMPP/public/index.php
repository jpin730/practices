<?php

// ENABLE DISPLAY ERRORS, XAMPP HAS AS DEFAULT
ini_set('display_errors', 1);
ini_set('display_startup_error', 1);
error_reporting(E_ALL);
 
require_once '../vendor/autoload.php';

session_start();

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__.'/..');
$dotenv->load();

// $dotenv = Dotenv\Dotenv::createUnsafeImmutable(__DIR__.'/..'); // ENABLE getenv() method
// var_dump(getenv('DB_HOST'));
// var_dump($_ENV['DB_HOST']);
// var_dump($_SERVER['DB_HOST']);

// ELOQUENT CONFIG
use Illuminate\Database\Capsule\Manager as Capsule;
use Aura\Router\RouterContainer;
use Zend\Diactoros\Response\RedirectResponse;

$capsule = new Capsule;
$capsule->addConnection([
    'driver'    => 'mysql',
    'host'      => $_ENV['DB_HOST'],
    'database'  => $_ENV['DB_NAME'],
    'username'  => $_ENV['DB_USER'],
    'password'  => $_ENV['DB_PASS'],
    'charset'   => 'utf8',
    'collation' => 'utf8_unicode_ci',
    'prefix'    => '',
]);
$capsule->setAsGlobal();
$capsule->bootEloquent();

$request = Zend\Diactoros\ServerRequestFactory::fromGlobals(
    $_SERVER,
    $_GET,
    $_POST,
    $_COOKIE,
    $_FILES
);

/* $route = $_GET['route'] ?? '/';

if ($route == '/') {
    require '../index.php';
}
elseif ($route == 'addJob') {
    require '../addJob.php';
} */

$routerContainer = new RouterContainer();
$map = $routerContainer->getMap();

/* REFERENCE: get(ROUTE_NAME, ROUTE_REQUESTED, RETURN||HANDLER); */
/* $map->get('index', '/PHP/', '../index.php'); */
$map->get('index', '/PHP/', [
    'controller' => 'App\Controllers\IndexController',
    'action' => 'indexAction'
]);
// ADD JOBS
$map->get('addJobs', '/PHP/jobs/add', [
    'controller' => 'App\Controllers\JobsController',
    'action' => 'getAddJobAction',
    'auth' => true
]);
$map->post('saveJobs', '/PHP/jobs/add', [
    'controller' => 'App\Controllers\JobsController',
    'action' => 'getAddJobAction',
    'auth' => true
]);
// ADD USERS
$map->get('addUser', '/PHP/users/add', [
    'controller' => 'App\Controllers\UsersController',
    'action' => 'getAddUser',
    'auth' => true
]);
$map->post('saveUser', '/PHP/users/save', [
    'controller' => 'App\Controllers\UsersController',
    'action' => 'postSaveUser',
    'auth' => true
]);
// LOGIN
$map->get('loginForm', '/PHP/login', [
    'controller' => 'App\Controllers\AuthController',
    'action' => 'getLogin'
]);
$map->post('auth', '/PHP/auth', [
    'controller' => 'App\Controllers\AuthController',
    'action' => 'postLogin'
]);
$map->get('logout', '/PHP/logout', [
    'controller' => 'App\Controllers\AuthController',
    'action' => 'getLogout'
]);
// ADMIN
$map->get('admin', '/PHP/admin', [
    'controller' => 'App\Controllers\AdminController',
    'action' => 'getIndex',
    'auth' => true
]);


$matcher = $routerContainer->getMatcher();
$route = $matcher->match($request);

/* function printElement(Printable $job) */
function printElement($job) {
    /* if ($job->visible == false) {
      return;
    } */
  
    echo '<li class="work-position">';
    
    /* echo '<h5>' . $job->getTitle() . '</h5>';
    echo '<p>' . $job->getDescription() . '</p>';
    echo '<p>' . $job->getDurationAsString() . '</p>'; */
    echo '<h5>' . $job->title . '</h5>';
    echo '<p>' . $job->description . '</p>';
    echo '<p>' . $job->getDurationAsString() . '</p>';

    echo '<strong>Achievements:</strong>';
    echo '<ul>';
    echo '<li>Lorem ipsum dolor sit amet, 80% consectetuer adipiscing elit.</li>';
    echo '<li>Lorem ipsum dolor sit amet, 80% consectetuer adipiscing elit.</li>';
    echo '<li>Lorem ipsum dolor sit amet, 80% consectetuer adipiscing elit.</li>';
    echo '</ul>';
    echo '</li>';
}

if (!$route) {
    echo 'No route';
}
else {
    $handlerData = $route->handler;
    $controllerName = $handlerData['controller'];
    $actionName = $handlerData['action'];
    $needsAuth = $handlerData['auth'] ?? false;

    $sessionUserId = $_SESSION['userId'] ?? null;
    if ($needsAuth && !$sessionUserId) {
        // echo 'Protected route';
        // sleep(1);
        $controller = new App\Controllers\AuthController;
        $response = $controller->getLogin();
        echo $response->getBody();
    }
    else {
        /* $controller = new $handlerData['controller']; */
        $controller = new $controllerName;
        $response = $controller->$actionName($request);
    
        foreach($response->getHeaders() as $name => $values)
        {
            foreach($values as $value) {
                header(sprintf('%s: %s', $name, $value), false);
            }
        }
        http_response_code($response->getStatusCode());
    
        echo $response->getBody();
    }
}

/* var_dump($request->getUri()->getPath()); */
/* var_dump($route->handler); */