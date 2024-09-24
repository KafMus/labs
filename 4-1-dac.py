import RPi.GPIO as GPIO
import time

def decToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

try:
    while True: 
        x = input()
        if x == "q":
            break
        x = int(x)
        GPIO.output(dac, decToBin(x))
        print(" ", 3.3/256 * x, " Volt")
except RuntimeError:
    print("Too big, number should be < 255")
except ValueError:
    print("Invalid value, should be pozitive integer number")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()