<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['action'])) {
        $action = $_POST['action'];

include("index.html");

        if ($action == "allumer") {
            // Exécuter la commande pour allumer la LED
            exec('sudo python3 led_on.py');
            echo "</br><img src='./img/on.png' alt='on' />";
        } elseif ($action == "eteindre") {
            // Exécuter la commande pour éteindre la LED
            exec('sudo python3 led_off.py');
            echo "</br><img src='./img/off.png' alt='off' />";
        }
    }
}
?>
