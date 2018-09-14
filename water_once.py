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

# Define the number of seconds that the pump should turn on for
pumpTimeOn = 10

# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# loop through pins and set mode and state to 'high'
for i in relayPinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

#pump that water boi
GPIO.output(2, GPIO.LOW)
print "relay 1 has been turned on"
time.sleep(pumpTimeOn);
GPIO.output(2, GPIO.HIGH)
print "relay 1 has been turned off"
plantLog = open("new-plant-log.csv","a")
plantLog.write(time.ctime() + "," + "water duration: ," + str(pumpTimeOn) + "\n")
