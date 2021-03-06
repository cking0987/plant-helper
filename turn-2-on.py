import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

#set current pin location
currentPin = 3

#set mode and state to HIGH
GPIO.setup(currentPin, GPIO.OUT)
GPIO.output(currentPin, GPIO.HIGH)

#turn it on
GPIO.output(currentPin, GPIO.LOW)
print "relay at pin number ", currentPin, " has been turned on"

# Reset GPIO settings
GPIO.cleanup()
