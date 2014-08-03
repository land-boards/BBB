import Adafruit_BBIO.PWM as PWM
import time

J18 = 'P8_19'
J25 = 'P8_13'

dutyCycle = 0.0

while True:
	dutyCycle = 0.0
	PWM.start(J18, dutyCycle, 1000, 1)
	while dutyCycle < 100.0:
		PWM.set_duty_cycle(J18, dutyCycle)
		time.sleep(0.1)
		dutyCycle += 5.0
	PWM.stop(J18)
	dutyCycle = 0.0
	PWM.start(J25, dutyCycle, 1000, 1)
	while dutyCycle < 100.0:
		PWM.set_duty_cycle(J25, dutyCycle)
		time.sleep(0.1)
		dutyCycle += 5.0
	PWM.stop(J25)

PWM.cleanup()
