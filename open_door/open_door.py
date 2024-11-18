import RPi.GPIO as GPIO
from fcntl import LOCK_NB, flock, LOCK_EX, LOCK_UN
from asyncio import sleep, to_thread

OPEN_DOOR_LOCKFILE_NAME = '/tmp/open_door.lock'

class FileMutex:
    def __init__(self, file):
        self.file = file

    async def __aenter__(self):
        self.fd = open(self.file, 'wb')
        def aquire_lock():
            flock(self.fd.fileno(), LOCK_EX)
        await to_thread(aquire_lock)

    async def __aexit__(self, _type, _value, _tb):
        flock(self.fd.fileno(), LOCK_UN)
        self.fd.close()

async def primePids():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        await sleep(0.5)

async def openSolenoid():
        await primePids()
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)

async def closeSolenoid():
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)

        await sleep(1)
        GPIO.cleanup()

async def openDoor():
    async with FileMutex(OPEN_DOOR_LOCKFILE_NAME):
        await openSolenoid()
        await sleep(10)
        await closeSolenoid()
