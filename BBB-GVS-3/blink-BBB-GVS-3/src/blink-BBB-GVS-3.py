import Adafruit_BBIO.GPIO as GPIO
import time

J1 = " P9_30"
J2 = "P9_27"
J3_3 = "P9_26"
J3_4 = "P9_24"
J4 = "P9_23"
J5_3 = "P9_21"
J5_4 = "P9_22"
J7 = "P9_15"
J8_3 = "P9_13"
J8_4 = "P9_11"
J9 = "P9_14"
J10 = "P9_12"
J12 = "P8_26"
J13 = "P8_19"
J14 = "P8_18"
J15 = "P8_17"
J16 = "P8_16"
J17 = "P8_15"
J18 = "P8_13"
J19 = "P8_12"
J20 = "P8_11"
J21 = "P8_09"
J22 = "P8_10"
J23 = "P8_07"
J24 = "P8_08"

def blinkLED(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.LOW)
	
GPIO.setup(J1, GPIO.OUT)
GPIO.setup(J2, GPIO.OUT)
GPIO.setup(J3_3, GPIO.OUT)
GPIO.setup(J3_4, GPIO.OUT)
GPIO.setup(J4, GPIO.OUT)
GPIO.setup(J5_3, GPIO.OUT)
GPIO.setup(J5_4, GPIO.OUT)
GPIO.setup(J7, GPIO.OUT)
GPIO.setup(J8_3, GPIO.OUT)
GPIO.setup(J8_4, GPIO.OUT)
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
GPIO.setup(J24, GPIO.OUT)

while True:
	blinkLED(J1)
	blinkLED(J3_3)
	blinkLED(J4)
	blinkLED(J5_4)
	blinkLED(J8_3)
	blinkLED(J9)
	blinkLED(J20)
	blinkLED(J22)
	blinkLED(J24)
	blinkLED(J23)
	blinkLED(J21)
	blinkLED(J12)
	blinkLED(J14)
	blinkLED(J16)
	blinkLED(J18)
	blinkLED(J19)
	blinkLED(J17)
	blinkLED(J15)
	blinkLED(J13)
	blinkLED(J10)
	blinkLED(J8_4)
	blinkLED(J7)
	blinkLED(J5_3)
	blinkLED(J3_4)
	blinkLED(J2)
