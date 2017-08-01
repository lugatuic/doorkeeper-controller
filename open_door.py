import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

GPIO.output(37, GPIO.HIGH)
GPIO.output(38, GPIO.HIGH)
time.sleep(5)

GPIO.output(37, GPIO.LOW)
GPIO.output(38, GPIO.LOW)

GPIO.cleanup()