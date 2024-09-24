import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
GPIO.output(24, GPIO.input(1))

