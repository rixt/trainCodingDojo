"""
This module demonstrates how-to read sensors and detect when the train is passing
"""

# External librarys
from time import sleep     # Import time library

# Library for controlling GPIO pins
import RPi.GPIO as GPIO  # https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

# BCM numbering - reference Physical pins on the Broadcom SOC
GPIO.setmode(GPIO.BCM)

SENSOR1 = 20
SENSOR2 = 21

# Set sensor 1 and 2 as input and Activate pull up resistor
GPIO.setup(SENSOR1, GPIO.IN, pull_upp_down=GPIO.PUD_UP)
GPIO.setup(SENSOR2, GPIO.IN, pull_upp_down=GPIO.PUD_UP)

while 1:  # Create an infinite loop

    if GPIO.input(SENSOR1) == 0:  # sensor 1 will report 0 if it is passed
        print "Sensor 1 Passing"
        sleep(.1)   # delay
    if GPIO.input(SENSOR2) == 0:  # sensor 2 will report 0 if it is passed
        sleep(.1)
        print "Sensor 2 Passing"

# Cleanup resources
GPIO.cleanup()
