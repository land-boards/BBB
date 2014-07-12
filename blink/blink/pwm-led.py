import Adafruit_BBIO.PWM as PWM
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
	
dutyCycle = 0.0

#optionally, you can set the frequency as well as the polarity from their defaults:
PWM.start("P8_19", dutyCycle, 1000, 1)

GPIO.setup(J37, GPIO.IN)

while GPIO.input(J37):
	PWM.set_duty_cycle("P8_19", dutyCycle)
	time.sleep(0.1)
	dutyCycle += 1.0
	if dutyCycle > 100.0:
		dutyCycle = 0

PWM.stop("P8_19")
PWM.cleanup()
