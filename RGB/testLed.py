import RPi.GPIO as GPIO
import time

# Configurer les broches GPIO
GPIO.setmode(GPIO.BCM)

# Configurer les broches des LED
GPIO.setup(21, GPIO.OUT)  # LED rouge
GPIO.setup(20, GPIO.OUT)  # LED verte
GPIO.setup(16, GPIO.OUT)  # LED bleue

try:
    # Allumer les LED une par une
    GPIO.output(21, GPIO.HIGH)  # LED rouge
    time.sleep(1)
    GPIO.output(21, GPIO.LOW)
    
    GPIO.output(20, GPIO.HIGH)  # LED verte
    time.sleep(1)
    GPIO.output(20, GPIO.LOW)

    GPIO.output(16, GPIO.HIGH)  # LED bleue
    time.sleep(1)
    GPIO.output(16, GPIO.LOW)

finally:
    GPIO.cleanup()
