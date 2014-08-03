import Adafruit_BBIO.PWM as PWM
import time

J18 = 'P8_19'
J25 = 'P8_13'

while True:
	PWM.stop('P8_13')
	PWM.cleanup()
	dutyCycle = 0.0
	PWM.start('P8_13', dutyCycle, 1000, 1)
	time.sleep(0.1)
	while dutyCycle < 100.0:
		PWM.set_duty_cycle('P8_13', dutyCycle)
		time.sleep(0.1)
		dutyCycle += 5.0
	PWM.stop('P8_13')
	PWM.stop('P8_19')
	PWM.cleanup()
	dutyCycle = 0.0
#	PWM.start('P8_19',0)
	PWM.start('P8_19', 0.0, 1000, 1)
	time.sleep(0.1)
	print 'thru'
	while dutyCycle < 100.0:
		PWM.set_duty_cycle('P8_19', dutyCycle)
		time.sleep(0.1)
		dutyCycle += 5.0
	PWM.stop('P8_19')

PWM.cleanup()
