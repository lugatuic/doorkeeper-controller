import RPi.GPIO as GPIO
from fcntl import flock, LOCK_EX, LOCK_UN
from time import sleep

class FileMutex:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.fd = open(self.file, 'wb')
        flock(self.fd.fileno(), LOCK_EX)

    def __exit__(self, _type, _value, _tb):
        flock(self.fd.fileno(), LOCK_UN)
        self.fd.close()

def primePids():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        sleep(0.5)

def openSolenoid():
        primePids()
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)

def closeSolenoid():
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)

        sleep(1)
        GPIO.cleanup()
