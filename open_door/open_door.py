import RPi.GPIO as GPIO
import time

def primePids():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        time.sleep(0.5)

def openSolenoid():
        primePids();
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)

def wait(seconds):
        time.sleep(seconds)

def closeSolenoid():
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)

        time.sleep(1)
        GPIO.cleanup()
