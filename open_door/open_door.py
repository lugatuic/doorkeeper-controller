import RPi.GPIO as GPIO
from time import sleep

def primePids():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        sleep(0.5)

def openSolenoid():
        primePids();
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)

def closeSolenoid():
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)

        sleep(1)
        GPIO.cleanup()
