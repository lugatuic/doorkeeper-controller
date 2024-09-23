# doorkeeper-controller
The controller program to control physical mechanism.

## Shell script
- UIC ID Cards have ? as the last character.
- The output of the EVDEV Driver is piped to this shell script.
- This script contains a list of UINs allowed to open the door.
- If the card is of an allowed UIN, the python scirpt to open the door is called.

## Deployment Information
- This service calls a shell script called `fuck-systemd.sh`
- This shell script calls the EVDEV Driver with its output piped to `the shell script in the submodule.
- Systemd messes up I/O redirection so the intermediary script is required.
