import Adafruit_BBIO.ADC as ADC
ADC.setup()
val0 = ADC.read("AIN0")
val1 = ADC.read("AIN1")
val2 = ADC.read("AIN2")
val3 = ADC.read("AIN3")
val4 = ADC.read("AIN4")
val5 = ADC.read("AIN5")
val6 = ADC.read("AIN6")

print 'val0 ',val0
print 'val1 ',val1
print 'val2 ',val2
print 'val3 ',val3
print 'val4 ',val4
print 'val5 ',val5
print 'val6 ',val6

errors = False

if val0 < 0.61 or val0 > 0.63:
	print 'error in val1'
	errors = True
if val1 < 0.12 or val1 > 0.13:
	print 'error in val1'
	errors = True
if val2 < 0.74 or val2 > 0.76:
	print 'error in val1'
	errors = True
if val3 < 0.24 or val3 > 0.26:
	print 'error in val1'
	errors = True
if val4 < 0.49 or val4 > 0.51:
	print 'error in val1'
	errors = True
if val5 < 0.37 or val5 > 0.38:
	print 'error in val1'
	errors = True
if val6 < 0.87 or val6 > 0.88:
	print 'error in val1'
	errors = True
if errors == True:
	print 'Had errors'
else:
	print 'No errors'
