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
J20 = "P8_11"		# VI-2 - D6
J21 = "P8_09"		# GY-2 - D22
J22 = "P8_10"		# WH-2 - D7
J23 = "P8_07"		# BL-2 - D23
J24 = "P8_08"		# BR-3 - D8
J12 = "P8_26"		# RD-3 - D24
J13 = "P8_19"		# OR-3 - D9
J14 = "P8_18"		# YL-3 - D25
J15 = "P8_17"		# GR-3 - D10
J16 = "P8_16"		# BU-3 - D26
J17 = "P8_15"		# VI-3 - D11
J18 = "P8_13"	    # GY-3 - D27
J19 = "P8_12"		# WH-3 - D12

D0 = "P9_30"		# GR-1 - D0
D1 = "P9_26"		# VI-1 - D1
D2 = "P9_23"		# WH-1 - D2
D3 = "P9_22"		# BR-2 - D3
D4 = "P9_13"		# OR-2 - D4
D5 = "P9_14"		# GR-2 - D5
D6 = "P8_11"		# RD-3 - D6
D7 = "P8_10"		# YL-3 - D7
D8 = "P8_08"		# BU-3 - D8
D9 = "P8_19"	    # GY-3 - D9
D10 = "P8_17"		# VI-2 - D10
D11 = "P8_15"		# WH-2 - D11
D12 = "P8_12"		# BR-3 - D12
D27 = "P8_13"		# BL-2 - D27
D26 = "P8_16"		# GY-2 - D26
D25 = "P8_18"		# WH-3 - D25
D24 = "P8_26"		# VI-3 - D24
D23 = "P8_07"		# GR-3 - D23
D22 = "P8_09"		# OR-3 - D22
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
GPIO.setup(D10, GPIO.OUT)
GPIO.setup(D11, GPIO.OUT)
GPIO.setup(D12, GPIO.OUT)
GPIO.setup(D27, GPIO.OUT)
GPIO.setup(D26, GPIO.OUT)
GPIO.setup(D25, GPIO.OUT)
GPIO.setup(D24, GPIO.OUT)
GPIO.setup(D23, GPIO.OUT)
GPIO.setup(D22, GPIO.OUT)
GPIO.setup(D21, GPIO.OUT)
GPIO.setup(D20, GPIO.OUT)
GPIO.setup(D19, GPIO.OUT)
GPIO.setup(D18, GPIO.OUT)
GPIO.setup(D17, GPIO.OUT)
GPIO.setup(D16, GPIO.OUT)

while True:
	blinkLED(D0)
	blinkLED(D1)
	blinkLED(D2)
	blinkLED(D3)
	blinkLED(D4)
	blinkLED(D5)
	blinkLED(D6)
	blinkLED(D7)
	blinkLED(D8)
	blinkLED(D9)
	blinkLED(D10)
	blinkLED(D11)
	blinkLED(D12)
	blinkLED(D27)
	blinkLED(D26)
	blinkLED(D25)
	blinkLED(D24)
	blinkLED(D23)
	blinkLED(D22)
	blinkLED(D21)
	blinkLED(D20)
	blinkLED(D19)
	blinkLED(D18)
	blinkLED(D17)
	blinkLED(D16)
