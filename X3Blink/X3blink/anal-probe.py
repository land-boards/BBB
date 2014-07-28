import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

J37 = "GPIO1_29"

GPIO.setup(J37, GPIO.IN)

ADC.setup()

while GPIO.input(J37):
	value = ADC.read("AIN1")
	voltage = value * 1.8
	print voltage
