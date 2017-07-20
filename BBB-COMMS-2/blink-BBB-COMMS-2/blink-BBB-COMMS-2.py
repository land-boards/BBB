# blink-BBB-COMMS-2.py
# Test the GPIO lines on the BBB
# Blink a High across the pins
import Adafruit_BBIO.GPIO as GPIO
import time

H3_3 = "P9_27"
H3_4 = "P9_23"
H4_3 = "P9_24"
H4_4 = "P9_26"
H5_3 = "P9_21"
H5_4 = "P9_22"
H6_3 = "P9_18"
H6_4 = "P9_17"
H7_3 = "P9_16"
H7_4 = "P9_15"
H8_3 = "P9_14"
H8_4 = "P9_12"
H9_3 = "P9_13"
H9_4 = "P9_11"

H11 = "P8_26"
H12 = "P8_18"
H13 = "P8_17"
H14 = "P8_16"
H15 = "P8_15"
H16 = "P8_12"
H17 = "P8_11"

def blinkLEDHigh(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.LOW)
	
def blinkLEDLow(channel):
	GPIO.output(channel, GPIO.LOW)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.HIGH)
	
GPIO.setup(H3_3, GPIO.OUT)
GPIO.setup(H3_4, GPIO.OUT)
GPIO.setup(H4_3, GPIO.OUT)
GPIO.setup(H4_4, GPIO.OUT)
GPIO.setup(H5_3, GPIO.OUT)
GPIO.setup(H5_4, GPIO.OUT)
# GPIO.setup(H6_3, GPIO.OUT)
# GPIO.setup(H6_4, GPIO.OUT)
GPIO.setup(H7_3, GPIO.OUT)
GPIO.setup(H7_4, GPIO.OUT)
GPIO.setup(H8_3, GPIO.OUT)
GPIO.setup(H8_4, GPIO.OUT)
GPIO.setup(H9_3, GPIO.OUT)
GPIO.setup(H9_4, GPIO.OUT)

GPIO.setup(H11, GPIO.OUT)
GPIO.setup(H12, GPIO.OUT)
GPIO.setup(H13, GPIO.OUT)
GPIO.setup(H14, GPIO.OUT)
GPIO.setup(H15, GPIO.OUT)
GPIO.setup(H16, GPIO.OUT)
GPIO.setup(H17, GPIO.OUT)

while True:
	blinkLEDHigh(H11)
	blinkLEDHigh(H13)
	blinkLEDHigh(H15)
	blinkLEDHigh(H17)
	blinkLEDHigh(H16)
	blinkLEDHigh(H14)
	blinkLEDHigh(H12)
	blinkLEDHigh(H3_3)
	blinkLEDHigh(H4_3)
	blinkLEDHigh(H5_3)
	# blinkLEDHigh(H6_3)
	# blinkLEDHigh(H6_4)
	blinkLEDHigh(H7_3)
	blinkLEDHigh(H8_3)
	blinkLEDHigh(H9_3)
	blinkLEDHigh(H9_4)
	blinkLEDHigh(H8_4)
	blinkLEDHigh(H7_4)
	blinkLEDHigh(H5_4)
	blinkLEDHigh(H4_4)
	blinkLEDHigh(H3_4)
