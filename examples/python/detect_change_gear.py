"""
This module is a combination of detect and motor module
"""

# External librarys
from time import sleep     # Import time library

# Library for controlling GPIO pins
import RPi.GPIO as GPIO  # https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

# NOTE: If MotorPower is set to high i can burn the motor
MOTORPOWER = 60

# BCM numbering - reference Physical pins on the Broadcom SOC
GPIO.setmode(GPIO.BCM)

# Pins for motor controller
STEPPIN_RIGHT = 23  # Blue 1
STEPPIN_LEFT = 24  # Blue 2
MOTORPOWER_PIN = 25  # Yellow

# Setup GPIO pins for Output
GPIO.setup(STEPPIN_RIGHT, GPIO.OUT)
GPIO.setup(STEPPIN_LEFT, GPIO.OUT)
GPIO.setup(MOTORPOWER_PIN, GPIO.OUT)

# GPIO.LOW and GPIO.HIGH specifies which way the motor rotates
# NOTE: NEVER set both to HIGH at the same time!!!
GPIO.output(STEPPIN_RIGHT, GPIO.LOW)
GPIO.output(STEPPIN_LEFT, GPIO.LOW)

# Pins for sensorss
SENSOR1 = 20
SENSOR2 = 21

# Set sensor 1 and 2 as input and Activate pull up resistor
GPIO.setup(SENSOR1, GPIO.IN, pull_upp_down=GPIO.PUD_UP)
GPIO.setup(SENSOR2, GPIO.IN, pull_upp_down=GPIO.PUD_UP)

# Function for driving motor
def drive_right(seconds_running_motor):
    """ Drive motor right """

    GPIO.output(STEPPIN_RIGHT, GPIO.HIGH)
    MOTOR_PWM.start(MOTORPOWER)
    print "righting running  motor "
    sleep(seconds_running_motor)
    GPIO.output(STEPPIN_RIGHT, GPIO.LOW)
    MOTOR_PWM.stop()


def drive_left(seconds_running_motor):
    """ Drive motor left """

    GPIO.output(STEPPIN_LEFT, GPIO.HIGH)
    MOTOR_PWM.start(MOTORPOWER)
    print "backwarding running motor"
    sleep(seconds_running_motor)
    GPIO.output(STEPPIN_LEFT, GPIO.LOW)
    MOTOR_PWM.stop()

GEARSTATE = 0

# PWM simulates analog output that RPi lacks
# By sending a pulse frequency
MOTOR_PWM = GPIO.PWM(MOTORPOWER_PIN, 100)

drive_left(0.5)

while 1:  # Create an infinite loop

    if GPIO.input(SENSOR1) == 0:  # sensor 1 will report 0 if it is passed
        print "Sensor 1 Passing"
        sleep(1)   # delay
    if GPIO.input(SENSOR2) == 0:  # sensor 2 will report 0 if it is passed
        print "Sensor 2 Passing"
        if GEARSTATE == 0:
            drive_right(0.6)
            GEARSTATE = 1
        else:
            drive_left(0.6)
            GEARSTATE = 0

        sleep(1)

# Clean up resources
GPIO.cleanup()
