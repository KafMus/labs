import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plot
import numpy as np

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def compOut():
    return GPIO.input(comp)

def adc():


    step = 128
    num = 0
    k = 0
    while k < 8:
        num += step
        sig = decToBin(num)
        GPIO.output(dac, sig)
        time.sleep(0.004)
        if compOut():
            num -= step
        step = int(step / 2)
        k += 1
    volt = num / 256 * 3.3
    print("Num = ", num, " Volt: ", volt)
    return num

try:
    print("Applying voltage 3.3V ...")
    GPIO.output(troyka, GPIO.HIGH)

    ExperimentBeginning = time.time()
    fileStr = open("../data.csv", "w")

    m = []
    flag = 0
    data = -1
    while True:
        data = adc()
        voltData = data / 256 * 3.3
        m.append(voltData)
        if voltData > 2.66: break
        
    
    print("Applying voltage 0.0V ...")
    GPIO.output(troyka, 0)

    flag = 0
    data = -1
    while True:
        data = adc()
        voltData = data / 256 * 3.3
        m.append(voltData)
        if voltData < 2.12: break
        

    for i in range(0, len(m)):
        if i == len(m) - 1:
            fileStr.write(str(m[i]))
        else:
            fileStr.write(str(m[i]) + "\n")
    
    ExperimentEnding = time.time()
    ExperimentDuration = ExperimentEnding - ExperimentBeginning
    Period = ExperimentDuration / len(m)
    DiscretizstionFrequency = 1 / Period
    QuantovStep = 3.3 / 256

    print("Experiment duration: ", ExperimentDuration)
    print("Period: ", Period)
    print("DiscretizstionFrequency: ", DiscretizstionFrequency)
    print("QuantovStep: ", QuantovStep)

    fileStr = open("../settings.csv", "w")

    fileStr.write(str(ExperimentDuration))
    fileStr.write(str(Period))
    fileStr.write(str(DiscretizstionFrequency))
    fileStr.write(str(QuantovStep))

finally:
    fileStr.close()
    GPIO.output(dac, 0)
    GPIO.cleanup()

    data = np.array(open("..//data.csv").read().split("\n"))
    data = [float(i) for i in data]

    plot.plot(data)
    plot.show()
