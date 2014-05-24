'''Code to read a switch and light an LED.

Based on code found at: https://github.com/adafruit/adafruit-beaglebone-io-python

============
Dependencies
============

Need to: 

* sudo apt-get install python-dev
* sudo apt-get install python-pip python2.7-dev
* sudo apt-get install python-rpi.gpio
* sudo pip install flask

====
Code
====
'''

import Adafruit_BBIO.GPIO as GPIO
import time

LED_PIN = "P8_10"
SWITCH_PIN = "P8_12"

class TalkToAPi:
	'''Simple code to talk to the low level bits of a BBB
	'''
	
	def __init__(self):
		'''constructor 
		'''
		GPIO.setmode(GPIO.BOARD)	# setup GPIO using Board numbering
		GPIO.setup(SWITCH_PIN, GPIO.IN)
		GPIO.setup(LED_PIN, GPIO.OUT)

	def getSwitchValue(self):
		'''Poll the value of a switch/pushbutton.
		Will probably replace this code later with an interrupt driven routine.

		:returns: True if the switch is pressed, false if the switch is not pressed
		'''
		if (GPIO.input(SWITCH_PIN) == 0):
			print 'getSwitchValue: Button pressed'
			return True
		else:
			print 'getSwitchValue: Button is not pressed'
			return False
			
	def controlLED(self, ledState):
		'''turns off or on a LED.
		The LED is pulled up to Vcc so it needs to be driven low to turn the LED on.
		
		:param ledState: True to turn the light on, false to turn light off
		'''
		ledVal = ledState
		if ledState == False:
			GPIO.output(LED_PIN, GPIO.HIGH)
		else:
			GPIO.output(LED_PIN, GPIO.LOW)
		return
		
	def getGPIOLibVersion(self):
		'''Returns the GPIO library version that is being used.
		
		:returns: GPIO library version as a string
		'''
		return GPIO.VERSION
		
	def stopUsingRPi(self):
		'''Free up the Raspbetty Pi pins when you are done using them
		'''
		GPIO.cleanup()
