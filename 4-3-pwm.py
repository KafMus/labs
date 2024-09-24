import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 1000)

while True:
    x = input()
    if x == "q":
        break
    x = int(x)
    p.start(x)


p.stop()
GPIO.cleanup()