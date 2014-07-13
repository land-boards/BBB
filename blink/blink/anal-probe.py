import Adafruit_BBIO.ADC as ADC

GPIO.setup(J37, GPIO.IN)

ADC.setup()

while GPIO.input(J37):
	value = ADC.read("AIN1")
	voltage = value * 1.8
	print voltage
