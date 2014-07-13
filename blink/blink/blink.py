import Adafruit_BBIO.GPIO as GPIO
import time

J8P3 = "GPIO3_16"	# ground pin is at wrong end
J9P3 = "GPIO0_15"	# UART1 Tx
J9P4 = "GPIO0_14"	# UART1 Rx
J11 = "GPIO1_17"
J12P3 = "GPIO0_3"	# UART2 Tx
J12P4 = "GPIO0_2"	# UART2 Rx
J13P3 = "GPIO0_4"	# I2C 1 SDA
J13P4 = "GPIO0_5"	# I2C 1 SCL
J14 = "GPIO1_16"
J15 = "GPIO1_28"
J19 = "GPIO0_22"	# EHRPWM2A
J21 = "GPIO0_27"
J22 = "GPIO2_1"
J23 = "GPIO1_15"
J24 = "GPIO0_23"	# EHRPWM2B
J25 = "GPIO2_4"		# TIMER6
J26 = "GPIO2_5"		# TIMER5
J27 = "GPIO2_3"		# TIMER7
J28 = "GPIO2_2"		# TIMER4
J37 = "GPIO1_29"


def blinkLED(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(channel, GPIO.LOW)
	
GPIO.setup(J8P3, GPIO.OUT)
GPIO.setup(J9P3, GPIO.OUT)
GPIO.setup(J9P4, GPIO.OUT)
GPIO.setup(J11, GPIO.OUT)
GPIO.setup(J12P3, GPIO.OUT)
GPIO.setup(J12P4, GPIO.OUT)
GPIO.setup(J13P3, GPIO.OUT)
GPIO.setup(J13P4, GPIO.OUT)
GPIO.setup(J14, GPIO.OUT)
GPIO.setup(J15, GPIO.OUT)
GPIO.setup(J19, GPIO.OUT)
GPIO.setup(J21, GPIO.OUT)
GPIO.setup(J22, GPIO.OUT)
GPIO.setup(J23, GPIO.OUT)
GPIO.setup(J24, GPIO.OUT)
GPIO.setup(J25, GPIO.OUT)
GPIO.setup(J26, GPIO.OUT)
GPIO.setup(J27, GPIO.OUT)
GPIO.setup(J28, GPIO.OUT)
GPIO.setup(J37, GPIO.OUT)

while True:
	# blinkLED(J8P3)
	# blinkLED(J9P3)
	# blinkLED(J9P4)
	blinkLED(J11)
	# blinkLED(J12P3)
	# blinkLED(J12P4)
	# blinkLED(J13P3)
	# blinkLED(J13P4)
	blinkLED(J14)
	blinkLED(J15)
	# blinkLED(J19)
	blinkLED(J21)
	blinkLED(J22)
	blinkLED(J23)
	blinkLED(J24)
	# blinkLED(J25)
	# blinkLED(J26)
	# blinkLED(J27)
	# blinkLED(J28)
	