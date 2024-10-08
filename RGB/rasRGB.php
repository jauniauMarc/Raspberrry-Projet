<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['rgbValue'])) {
        $rgbValue = $_POST['rgbValue'];
        list($r, $g, $b) = explode(',', $rgbValue); // Sépare les valeurs R, G, B

        // Appelle le script Python en lui passant les valeurs R, G, B
        $command = escapeshellcmd("sudo python3 control_led.py $r $g $b 2>&1");
        $output = shell_exec($command);
        
        // Afficher la sortie pour le débogage
        echo "<pre>$output</pre>"; 
        
        // Redirige vers index2.html après 2 secondes
        header("Refresh: 1; url=index2.html");
        exit(); // Assure-toi d'ajouter exit() pour arrêter le script ici
    }
}
?>
