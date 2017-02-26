"""
Stop the train in channel 3 Blue
"""

# External librarys
from subprocess import call

def send_once(command):
    """
    Send single call to IR LED.
    """
    call(['irsend', 'SEND_ONCE', 'LEGO_Single_Output', command])


send_once('3B_BRAKE')

