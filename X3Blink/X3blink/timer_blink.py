import Adafruit_BBIO.GPIO as GPIO
import time


J29 = "TIMER6"		# TIMER6
J30 = "TIMER5"		# TIMER5
J21 = "TIMER7"		# TIMER7
J32 = "TIMER4"		# TIMER4


def blinkLED(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(channel, GPIO.LOW)
	
GPIO.setup(J29, GPIO.OUT)
GPIO.setup(J30, GPIO.OUT)
GPIO.setup(J31, GPIO.OUT)
GPIO.setup(J28, GPIO.OUT)

while True:
	blinkLED(J29)
	blinkLED(J30)
	blinkLED(J31)
	blinkLED(J32)
	
GPIO.cleanup()
