"""
This module demostrates how-to start and stop the motor
"""

# External librarys
import time

# Library for controlling GPIO pins
import RPi.GPIO as GPIO  # https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

# Pins for motor controller
STEPPIN_RIGHT = 23  # Blue 1
STEPPIN_LEFT = 24  # Blue 2
MOTORPOWER_PIN = 25  # Yellow

# NOTE: If MotorPower is set to high i can burn the motor
MOTORPOWER = 60

# BCM numbering - reference Physical pins on the Broadcom SOC
GPIO.setmode(GPIO.BCM)

# Setup GPIO pins for Output
GPIO.setup(STEPPIN_RIGHT, GPIO.OUT)
GPIO.setup(STEPPIN_LEFT, GPIO.OUT)
GPIO.setup(MOTORPOWER_PIN, GPIO.OUT)

# GPIO.LOW and GPIO.HIGH specifies which way the motor rotates
# NOTE: NEVER set both to HIGH at the same time!!!
GPIO.output(STEPPIN_RIGHT, GPIO.LOW)
GPIO.output(STEPPIN_LEFT, GPIO.LOW)

# PWM simulates analog output that RPi lacks
# By sending a pulse frequency
MOTOR_PWM = GPIO.PWM(MOTORPOWER_PIN, 100)

# Function for driving motor
def drive_right(seconds_running_motor):
    """ Drive motor right """

    GPIO.output(STEPPIN_RIGHT, GPIO.HIGH)
    MOTOR_PWM.start(MOTORPOWER)
    print "Running  motor right"
    time.sleep(seconds_running_motor)
    GPIO.output(STEPPIN_RIGHT, GPIO.LOW)
    MOTOR_PWM.stop()

def drive_left(seconds_running_motor):
    """ Drive motor left """

    GPIO.output(STEPPIN_LEFT, GPIO.HIGH)
    MOTOR_PWM.start(MOTORPOWER)
    print "Running motor left"
    time.sleep(seconds_running_motor)
    GPIO.output(STEPPIN_LEFT, GPIO.LOW)
    MOTOR_PWM.stop()

# Runnes the motor 10 times left and right
for x in range(0, 10):
    print "Right motor "
    drive_right(0.5)

    time.sleep(1)

    print "Left motor"
    drive_left(0.5)

    time.sleep(1)

# Cleanup resources
GPIO.cleanup()
