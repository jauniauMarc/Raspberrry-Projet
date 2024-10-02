<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['action'])) {
        $action = $_POST['action'];
        
        if ($action == "allumer") {
            // Exécuter la commande pour allumer la LED
            exec('sudo python3 led_on.py');
            echo "<p>LED allumée !</p>";
        } elseif ($action == "eteindre") {
            // Exécuter la commande pour éteindre la LED
            exec('sudo python3 led_off.py');
            echo "<p>LED éteinte !</p>";
        }
    }
}
?>
