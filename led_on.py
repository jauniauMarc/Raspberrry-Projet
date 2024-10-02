import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Utilisation des numéros de pin BCM
GPIO.setup(21, GPIO.OUT)  # Définit la broche 17 en sortie

GPIO.output(21, GPIO.HIGH)  # Allume la LED
