#!/usr/bin/env python
# Blink an LED on the I2CIO-8 card
#
# Hardware
#	
# 	Physically connected to I2C1 port but is I2C-2 from the software
# 
# Run using
#	python MCP23008_ex.py
#
# Edit /boot/uboot/uEnv.txt
# 	nano /boot/uboot/uEnv.txt
# 	optargs=quiet drm.debug-7 capemgr.enable_partno=BB-I2C0,BB-I2C1,BB-I2C2

from smbus import SMBus
import time

def main():
    '''
    Main program function
    '''
    # Define registers values from datasheet
    IODIR = 0x00	# IO direction A - 1= input 0 = output
    IPOL = 0x01		# Input polarity
    GPINTEN = 0x02	# Interrupt-onchangeA
    DEFVAL = 0x03	# Default value
    INTCON = 0x04	# Interrupt control register
    IOCON = 0x05	# Configuration register
    GPPU = 0x06		# Pull-up resistors
    INTF = 0x07		# Interrupt condition
    INTCAP = 0x08	# Interrupt capture
    GPIO = 0x09		# Data port
    OLATA = 0x0A	# Output latches

    i2cbus = SMBus(2)  # Create a new I2C bus
    i2caddress = 0x20  # Address of MCP23008 device

    i2cbus.write_byte_data(i2caddress, IOCON, 0x02)  # Update configuration register

    i2cbus.write_word_data(i2caddress, IODIR, 0xFF00)  # Set Port A as outputs and Port B as
 inputs

    while (True):
        # portb = i2cbus.read_byte_data(i2caddress, GPIO)  # Read the value of Port B
        # print(portb) # print the value of GPIO

        i2cbus.write_byte_data(i2caddress, GPIO, 0x01)  # Set pin 1 to on
        time.sleep(0.5)  # Wait 500ms

        i2cbus.write_byte_data(i2caddress, GPIO, 0x00)  # Set pin 1 to off
        time.sleep(0.5)  # Wait 500ms


if __name__ == "__main__":
    main()
