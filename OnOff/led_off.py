import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)  # Éteint la LED
GPIO.cleanup()  # Nettoie la configuration GPIO
