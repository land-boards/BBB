import Adafruit_BBIO.PWM as PWM
import time

dutyCycle = 0.0

#optionally, you can set the frequency as well as the polarity from their defaults:

PWM.start("P8_13", dutyCycle, 1000, 1)

while 1:
	PWM.set_duty_cycle("P8_13", dutyCycle)
	time.sleep(0.1)
	dutyCycle += 5.0
	if dutyCycle > 100.0:
		dutyCycle = 0

PWM.stop("P8_13")
PWM.cleanup()
