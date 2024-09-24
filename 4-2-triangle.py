import RPi.GPIO as GPIO
import time

def decToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

try:
    step = 3.3 / 256
    T = int(input("Period in seconds: "))
    t = T / 256
    x = 0
    while True:
        for i in range (0, 128):
            GPIO.output(dac, decToBin(int(x / step)))
            x += step
            time.sleep(t)
        for i in range (128, 255):
            GPIO.output(dac, decToBin(int(x / step)))
            x -= step
            time.sleep(t)
        x = 0
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()