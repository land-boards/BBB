import Adafruit_BBIO.GPIO as GPIO
import time

J8 = "GPIO3_16"
J9 = "GPIO3_19"
J10 = "GPIO1_17"
J11_3 = "GPIO0_15"
J11_4 = "GPIO0_14"
J12_3 = "GPIO0_3"
J12_4 = "GPIO0_2"
J13_3 = "GPIO0_12"
J13_4 = "GPIO0_13"
J14 = "GPIO1_16"
J15 = "GPIO1_28"
J16_3 = "GPIO0_31"
J16_4 = "GPIO0_30"
J17 = "GPIO1_29"
J18 = "GPIO0_22"
J19 = "GPIO2_1"
J20 = "GPIO0_27"
J21 = "GPIO1_14"
J22 = "GPIO1_15"
J25 = "GPIO0_23"
J26 = "GPIO0_26"
J27 = "GPIO1_13"
J28 = "GPIO1_12"
J29 = "GPIO2_5"
J30 = "GPIO2_3"
J31 = "GPIO1_3"
J32 = "GPIO2_4"

def blinkLED(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.LOW)
	
GPIO.setup(J8, GPIO.OUT)
GPIO.setup(J9, GPIO.OUT)
GPIO.setup(J10, GPIO.OUT)
GPIO.setup(J11_3, GPIO.OUT)
GPIO.setup(J11_4, GPIO.OUT)
GPIO.setup(J12_3, GPIO.OUT)
GPIO.setup(J12_4, GPIO.OUT)
GPIO.setup(J13_3, GPIO.OUT)
GPIO.setup(J13_4, GPIO.OUT)
GPIO.setup(J14, GPIO.OUT)
GPIO.setup(J15, GPIO.OUT)
GPIO.setup(J16_3, GPIO.OUT)
GPIO.setup(J16_4, GPIO.OUT)
GPIO.setup(J17, GPIO.OUT)
GPIO.setup(J18, GPIO.OUT)
GPIO.setup(J19, GPIO.OUT)
GPIO.setup(J20, GPIO.OUT)
GPIO.setup(J21, GPIO.OUT)
GPIO.setup(J22, GPIO.OUT)
GPIO.setup(J25, GPIO.OUT)
GPIO.setup(J26, GPIO.OUT)
GPIO.setup(J27, GPIO.OUT)
GPIO.setup(J28, GPIO.OUT)
GPIO.setup(J29, GPIO.OUT)
GPIO.setup(J30, GPIO.OUT)
GPIO.setup(J31, GPIO.OUT)
GPIO.setup(J32, GPIO.OUT)

while True:
	blinkLED(J8)
	blinkLED(J9)
	blinkLED(J10)
	blinkLED(J11_3)
	blinkLED(J11_4)
	blinkLED(J12_3)
	blinkLED(J12_4)
	blinkLED(J13_3)
	blinkLED(J13_4)
	blinkLED(J14)
	blinkLED(J15)
	blinkLED(J16_3)
	blinkLED(J16_4)
	blinkLED(J17)
	blinkLED(J18)
	blinkLED(J19)
	blinkLED(J20)
	blinkLED(J21)
	blinkLED(J22)
	blinkLED(J23)
	blinkLED(J24)
	blinkLED(J25)
	blinkLED(J26)
	blinkLED(J27)
	blinkLED(J28)
	blinkLED(J29)
	blinkLED(J30)
	blinkLED(J31)
	blinkLED(J32)
