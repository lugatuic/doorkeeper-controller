#!/bin/sh

while true
do
	~/.cargo/bin/door-driver /dev/input/event0 | ./card_reader.sh
done
