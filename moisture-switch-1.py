#!/usr/bin/python

# Start by importing the libraries we want to use
import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time # This is the time library, we need this so we can use the sleep function

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# init list with pin numbers
relayPinList = [2, 3, 4, 17, 27, 22, 10, 9]

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 14
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# loop through pins and set mode and state to 'high'
for i in relayPinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# This is our callback function, this function will be called every time there is a change on the specified GPIO channel
def callback(channel):
	if GPIO.input(channel):
		print "low moisture detected"
		GPIO.output(2, GPIO.LOW)
		print "relay 1 has been turned on"
		time.sleep(2);
		GPIO.output(2, GPIO.HIGH)
		print "relay 1 has been turned off"
	else:
		print "moisture detected"

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, callback)

# This is an infinte loop to keep our script running
while True:
	# This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
	time.sleep(0.1)
