import Adafruit_BBIO.GPIO as GPIO
import time

J37 = "GPIO1_29"
J35 = "GPIO1_0"
J33 = "GPIO1_1"
J31 = "GPIO1_4"
J15 = "GPIO1_28"
J14 = "GPIO1_16"

GPIO.setup(J37, GPIO.OUT)
GPIO.setup(J15, GPIO.OUT)
GPIO.setup(J14, GPIO.OUT)

while True:
	GPIO.output(J37, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(J37, GPIO.LOW)
	GPIO.output(J15, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(J15, GPIO.LOW)
	GPIO.output(J14, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(J14, GPIO.LOW)

