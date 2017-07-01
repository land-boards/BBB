import Adafruit_BBIO.GPIO as GPIO
import time

J1 = "P9_30"		# GR-1 - D0
J2 = "P9_27"		# BL-1 - D16
J3_3 = "P9_26"		# VI-1 - D1
J3_4 = "P9_24"		# GY-1 - D17
J4 = "P9_23"		# WH-1 - D2
J5_3 = "P9_21"		# BL-1 - D18
J5_4 = "P9_22"		# BR-2 - D3
J7 = "P9_15"		# RD-2 - D19
J8_3 = "P9_13"		# OR-2 - D4
J8_4 = "P9_11"		# YL-2 - D20
J9 = "P9_14"		# GR-2 - D5
J10 = "P9_12"		# BU-2 - D21
J12 = "P8_26"		# RD-3 - D6
J13 = "P8_19"		# OR-3 - D22
J14 = "P8_18"		# YL-3 - D7
J15 = "P8_17"		# GR-3 - D23
J16 = "P8_16"		# BU-3 - D8
J17 = "P8_15"		# VI-3 - D24
J18 = "P8_13"	    # GY-3 - D9
J19 = "P8_12"		# WH-3 - D25
J20 = "P8_11"		# VI-2 - D10
J21 = "P8_09"		# GY-2 - D26
J22 = "P8_10"		# WH-2 - D11
J23 = "P8_07"		# BL-2 - D27
J24 = "P8_08"		# BR-3 - D12

D0 = "P9_30"		# GR-1 - D0
D1 = "P9_26"		# VI-1 - D1
D2 = "P9_23"		# WH-1 - D2
D3 = "P9_22"		# BR-2 - D3
D4 = "P9_13"		# OR-2 - D4
D5 = "P9_14"		# GR-2 - D5
D6 = "P8_26"		# RD-3 - D6
D7 = "P8_18"		# YL-3 - D7
D8 = "P8_16"		# BU-3 - D8
D9 = "P8_13"	    # GY-3 - D9
D10 = "P8_11"		# VI-2 - D10
D11 = "P8_10"		# WH-2 - D11
D12 = "P8_08"		# BR-3 - D12
D27 = "P8_07"		# BL-2 - D27
D26 = "P8_09"		# GY-2 - D26
D25 = "P8_12"		# WH-3 - D25
D24 = "P8_15"		# VI-3 - D24
D23 = "P8_17"		# GR-3 - D23
D22 = "P8_19"		# OR-3 - D22
D21 = "P9_12"		# BU-2 - D21
D20 = "P9_11"		# YL-2 - D20
D19 = "P9_15"		# RD-2 - D19
D18 = "P9_21"		# BL-1 - D18
D17 = "P9_24"		# GY-1 - D17
D16 = "P9_27"		# BL-1 - D16


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
	blinkLED(J21)
	blinkLED(J23)
	blinkLED(J24)
	blinkLED(J22)
	blinkLED(J20)
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
