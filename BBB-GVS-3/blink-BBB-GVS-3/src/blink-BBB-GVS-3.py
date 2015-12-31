import Adafruit_BBIO.GPIO as GPIO
import time

J1 = "GPIO3_16"
J2 = "GPIO3_19"
J4 = "GPIO1_17"
J7 = "GPIO1_16"
J9 = "GPIO1_18"
J10 = "GPIO1_28"
J12 = "GPIO1_29"
J13 = "GPIO0_22"
J14 = "GPIO2_1"
J15 = "GPIO0_27"
J16 = "GPIO1_14"
J17 = "GPIO1_15"
J18 = "GPIO0_23"
J19 = "GPIO1_12"
J20 = "GPIO1_13"
J21 = "GPIO2_5"
J22 = "GPIO2_4"
J23 = "GPIO2_2"
J24 = "GPIO2_3"

def blinkLED(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.LOW)
	
GPIO.setup(J1, GPIO.OUT)
GPIO.setup(J2, GPIO.OUT)
GPIO.setup(J4, GPIO.OUT)
GPIO.setup(J9, GPIO.OUT)
GPIO.setup(J10, GPIO.OUT)
GPIO.setup(J12, GPIO.OUT)
GPIO.setup(J13, GPIO.OUT)
GPIO.setup(J14, GPIO.OUT)
GPIO.setup(J15, GPIO.OUT)
GPIO.setup(J16, GPIO.OUT)
GPIO.setup(J17, GPIO.OUT)
GPIO.setup(J18, GPIO.OUT)
GPIO.setup(J19, GPIO.OUT)
GPIO.setup(J20, GPIO.OUT)
GPIO.setup(J21, GPIO.OUT)
GPIO.setup(J22, GPIO.OUT)
GPIO.setup(J23, GPIO.OUT)

while True:
	blinkLED(J1)
	blinkLED(J2)
	blinkLED(J4)
	blinkLED(J9)
	blinkLED(J10)
	blinkLED(J12)
	blinkLED(J13)
	blinkLED(J14)
	blinkLED(J15)
	blinkLED(J16)
	blinkLED(J17)
	blinkLED(J18)
	blinkLED(J19)
	blinkLED(J20)
	blinkLED(J21)
	blinkLED(J22)
	blinkLED(J23)
