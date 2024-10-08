import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)          # Utilise la numérotation BCM
GPIO.setup(21, GPIO.OUT)       # Configure la broche 21 comme sortie
GPIO.output(21, GPIO.HIGH)     # Allume la LED
