from open_door import closeSolenoid, openSolenoid, FileMutex, OPEN_DOOR_LOCKFILE_NAME
from time import sleep

with FileMutex(OPEN_DOOR_LOCKFILE_NAME):
    openSolenoid()
    sleep(10)
    closeSolenoid()
