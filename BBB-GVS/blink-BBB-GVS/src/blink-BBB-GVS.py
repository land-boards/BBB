import Adafruit_BBIO.GPIO as GPIO
import time

J8 = "P9_30"
J9 = "P9_27"
J10 = "P9_23"
J11_3 = "P9_24"
J11_4 = "P9_26"
J12_3 = "P9_21"
J12_4 = "P9_22"
J13_3 = "P9_18"
J13_4 = "P9_17"
J14 = "P9_15"
J15 = "P9_12"
J16_3 = "P9_13"
J16_4 = "P9_11"
J17 = "P8_26"
J18 = "P8_19"
J19 = "P8_18"
J20 = "P8_17"
J21 = "P8_16"
J22 = "P8_15"
J25 = "P8_13"
J26 = "P8_14"
J27 = "P8_11"
J28 = "P8_12"
J29 = "P8_9"
J30 = "P8_8"
J31 = "P8_7"
J32 = "P8_10"

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
# GPIO.setup(J13_3, GPIO.OUT)
# GPIO.setup(J13_4, GPIO.OUT)
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
	# blinkLED(J13_3)
	# blinkLED(J13_4)
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
	blinkLED(J25)
	blinkLED(J26)
	blinkLED(J27)
	blinkLED(J28)
	blinkLED(J29)
	blinkLED(J30)
	blinkLED(J31)
	blinkLED(J32)
