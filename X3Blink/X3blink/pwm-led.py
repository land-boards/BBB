import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

J19 = "GPIO0_22"	# EHRPWM2A
J24 = "GPIO0_23"	# EHRPWM2B
J37 = "GPIO1_29"
	
dutyCycle = 0.0

#optionally, you can set the frequency as well as the polarity from their defaults:
PWM.start("P8_19", dutyCycle, 1000, 1)

GPIO.setup(J37, GPIO.IN)

while GPIO.input(J37):
	PWM.set_duty_cycle("P8_19", dutyCycle)
	time.sleep(0.1)
	dutyCycle += 5.0
	if dutyCycle > 100.0:
		dutyCycle = 0

PWM.stop("P8_19")
PWM.cleanup()
