import RPi.GPIO as GPIO
import sys
import time

# Récupérer les valeurs RGB depuis les arguments
r_value = int(sys.argv[1])
g_value = int(sys.argv[2])
b_value = int(sys.argv[3])

# Configurer les broches GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)  # LED rouge (Broche 21)
GPIO.setup(20, GPIO.OUT)  # LED verte (Broche 20)
GPIO.setup(16, GPIO.OUT)  # LED bleue (Broche 16)

# Utilisation de PWM pour ajuster l'intensité de la LED
red_led = GPIO.PWM(21, 100)  # PWM sur la broche 21 à 100Hz
green_led = GPIO.PWM(20, 100)  # PWM sur la broche 20 à 100Hz
blue_led = GPIO.PWM(16, 100)  # PWM sur la broche 16 à 100Hz

# Démarrage du PWM avec une intensité initiale de 0
red_led.start(0)
green_led.start(0)
blue_led.start(0)

try:
    # Ajuster l'intensité en fonction des valeurs RGB (0 à 100 pour le PWM)
    red_led.ChangeDutyCycle(r_value / 255 * 100)
    green_led.ChangeDutyCycle(g_value / 255 * 100)
    blue_led.ChangeDutyCycle(b_value / 255 * 100)

    # Pour vérifier les valeurs PWM
    print(f"Intensité LED Rouge: {r_value / 255 * 100}%")
    print(f"Intensité LED Verte: {g_value / 255 * 100}%")
    print(f"Intensité LED Bleue: {b_value / 255 * 100}%")

    # Garder les LEDs allumées pendant 5 secondes
    time.sleep(5)

finally:
    # Nettoyer les GPIO lorsque l'exécution est terminée
    red_led.stop()
    green_led.stop()
    blue_led.stop()
    GPIO.cleanup()
