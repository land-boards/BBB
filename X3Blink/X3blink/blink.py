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

def blinkLED(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(channel, GPIO.LOW)
	
GPIO.setup(J17, GPIO.OUT)
GPIO.setup(J19, GPIO.OUT)
GPIO.setup(J20, GPIO.OUT)
GPIO.setup(J21, GPIO.OUT)
GPIO.setup(J22, GPIO.OUT)
GPIO.setup(J26, GPIO.OUT)
GPIO.setup(J27, GPIO.OUT)
GPIO.setup(J28, GPIO.OUT)

while True:
	blinkLED(J9)
	blinkLED(J10)
	blinkLED(J14)
	blinkLED(J15)
	blinkLED(J17)
	blinkLED(J19)
	blinkLED(J20)
	blinkLED(J21)
	blinkLED(J22)
	blinkLED(J26)
	blinkLED(J27)
	blinkLED(J28)
	