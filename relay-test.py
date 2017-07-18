#!/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
time.sleep(3)

timings = [0.5,0.4,0.3,0.2,0.1,0.09,0.05,0.01]
timings3 = [5, 1, 1, 1]
timings2 = [0.1,0.1,0.3,0.1,0.1,0.3,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3,0.1,0.1,0.3,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3]

for x in timings3:
    GPIO.output(37, GPIO.HIGH)
    GPIO.output(38, GPIO.HIGH)
    time.sleep(x)

    GPIO.output(37, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    time.sleep(x)

time.sleep(1)
time.sleep(1)
GPIO.cleanup()
