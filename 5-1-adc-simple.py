import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)



GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(0, 256):
        sig = decToBin(i)
        GPIO.output(dac, sig)
        volt = i / 256 * 3.3
        time.sleep(0.1)
        print(GPIO.input(comp))
        if  GPIO.input(comp):
            print("ADC val = ", i, " ", sig, " Voltage ", volt)
            break
        
try:
    while True:
        print()
        time.sleep(1)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
