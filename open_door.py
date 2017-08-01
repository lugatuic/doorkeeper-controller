import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
time.sleep(0.5)

GPIO.output(37, GPIO.HIGH)
GPIO.output(38, GPIO.HIGH)
time.sleep(5)

GPIO.output(37, GPIO.LOW)
GPIO.output(38, GPIO.LOW)

time.sleep(1)
GPIO.cleanup()