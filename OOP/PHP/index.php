<?php
require_once('car.php');
require_once('carX.php');
require_once('carPool.php');
require_once('account.php');

$carX = new CarX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Spark");
$carX->printDataCar();

$carPool = new CarX("TYU567", new Account("Andrea Ferran", "AND765"), "Dodge", "Attitude");
$carPool->printDataCar();
?>