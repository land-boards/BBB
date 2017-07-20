# blink-BBB-COMMS-2.py
# Test the GPIO lines on the BBB
# Blink a High across the pins
import Adafruit_BBIO.GPIO as GPIO
import time

D0 = "P8_26"
D1 = "P8_17"
D2 = "P8_15"
D3 = "P8_11"
D4 = "P9_23"
D5 = "P9_26"
D6 = "P9_22"
D7 = "P9_15"
D8 = "P9_12"
D9 = "P9_11"

D16 = "P8_18"
D17 = "P8_16"
D18 = "P8_12"
D19 = "P9_27"
D20 = "P9_24"
D21 = "P9_21"
D22 = "P9_16"
D23 = "P9_14"
D24 = "P9_13"

def blinkLEDHigh(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.LOW)
	
def blinkLEDLow(channel):
	GPIO.output(channel, GPIO.LOW)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.HIGH)
	
GPIO.setup(D0, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)
GPIO.setup(D4, GPIO.OUT)
GPIO.setup(D5, GPIO.OUT)
GPIO.setup(D6, GPIO.OUT)
GPIO.setup(D7, GPIO.OUT)
GPIO.setup(D8, GPIO.OUT)
GPIO.setup(D9, GPIO.OUT)
GPIO.setup(D16, GPIO.OUT)
GPIO.setup(D17, GPIO.OUT)
GPIO.setup(D18, GPIO.OUT)
GPIO.setup(D19, GPIO.OUT)
GPIO.setup(D20, GPIO.OUT)
GPIO.setup(D21, GPIO.OUT)
GPIO.setup(D22, GPIO.OUT)
GPIO.setup(D23, GPIO.OUT)
GPIO.setup(D24, GPIO.OUT)

while True:
	blinkLEDHigh(D0)
	blinkLEDHigh(D1)
	blinkLEDHigh(D2)
	blinkLEDHigh(D3)
	blinkLEDHigh(D4)
	blinkLEDHigh(D5)
	blinkLEDHigh(D6)
	blinkLEDHigh(D7)
	blinkLEDHigh(D8)
	blinkLEDHigh(D9)

	blinkLEDHigh(D24)
	blinkLEDHigh(D23)
	blinkLEDHigh(D22)
	blinkLEDHigh(D21)
	blinkLEDHigh(D20)
	blinkLEDHigh(D19)
	blinkLEDHigh(D18)
	blinkLEDHigh(D17)
	blinkLEDHigh(D16)
	# blinkLEDHigh(H6_3)
	# blinkLEDHigh(H6_4)
