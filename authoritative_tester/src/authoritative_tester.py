#!/usr/bin/env python

from card_config import *
from main_menu import MainMenu
from analog_menu import AnalogMenu
from gpio_blink_menu import GpioBlinkMenu
from pwm_dim_menu import PwmDimMenu
import curses

def init_screen():
    screen = curses.initscr()
    screen.nodelay(True)
    curses.noecho()
    return screen

if __name__ == '__main__':
    screen = init_screen()
    main_menu = MainMenu(screen, {
        'Test Analog Jacks': (lambda: AnalogMenu(screen, JACK_TO_ANALOG)),
        'Test GPIO Output': (lambda: GpioBlinkMenu(screen, JACK_TO_GPIO)),
        'Test PWM Output': (lambda: PwmDimMenu(screen, JACK_TO_PWM)),
    })
    main_menu.show()
