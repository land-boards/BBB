#!/usr/bin/env python

from card_config import *
from main_menu import MainMenu
from analog_menu import AnalogMenu
import curses

def init_screen():
    screen = curses.initscr()
    screen.nodelay(True)
    curses.noecho()
    return screen

if __name__ == '__main__':
    screen = init_screen()
    main_menu = MainMenu(screen, {
        'Test Analog Jacks': (lambda: AnalogMenu(screen, JACK_TO_ANALOG))
    })
    main_menu.show()
