import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

J17 = "GPIO1_29"
J19 = "GPIO2_1"
J20 = "GPIO0_27"
J21 = "GPIO1_14"
J22 = "GPIO1_15"
J26 = "GPIO0_26"
J27 = "GPIO1_13"
J28 = "GPIO1_12"

GPIO.setup(J17, GPIO.OUT)
GPIO.setup(J19, GPIO.OUT)
GPIO.setup(J20, GPIO.OUT)
GPIO.setup(J21, GPIO.OUT)
GPIO.setup(J22, GPIO.OUT)
GPIO.setup(J26, GPIO.OUT)
GPIO.setup(J27, GPIO.OUT)
GPIO.setup(J28, GPIO.OUT)
ADC.setup()

while True:
	value = ADC.read("AIN1")
	if value > 0.5/8.0:
		GPIO.output(J17, GPIO.HIGH)
	else:
		GPIO.output(J17, GPIO.LOW)
	if value > 1.5/8.0:
		GPIO.output(J19, GPIO.HIGH)
	else:
		GPIO.output(J19, GPIO.LOW)
	if value > 2.5/8.0:
		GPIO.output(J20, GPIO.HIGH)
	else:
		GPIO.output(J20, GPIO.LOW)
	if value > 3.5/8.0:
		GPIO.output(J21, GPIO.HIGH)
	else:
		GPIO.output(J21, GPIO.LOW)
	if value > 4.5/8.0:
		GPIO.output(J22, GPIO.HIGH)
	else:
		GPIO.output(J22, GPIO.LOW)
	if value > 5.5/8.0:
		GPIO.output(J26, GPIO.HIGH)
	else:
		GPIO.output(J26, GPIO.LOW)
	if value > 6.5/8.0:
		GPIO.output(J27, GPIO.HIGH)
	else:
		GPIO.output(J27, GPIO.LOW)
	if value > 7.5/8.0:
		GPIO.output(J28, GPIO.HIGH)
	else:
		GPIO.output(J28, GPIO.LOW)
