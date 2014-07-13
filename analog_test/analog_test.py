#!/usr/bin/env python

from analog_config import *
import curses
import Adafruit_BBIO.ADC as ADC

if __name__ == '__main__':
    ADC.setup()
    screen = curses.initscr()
    curses.noecho()
    screen.nodelay(True)
    pressed_key = 0
    EXIT_KEY = ord(EXIT_KEY_NAME)

    while pressed_key != EXIT_KEY:
        pressed_key = screen.getch()
        screen.clear()
        for i, input_line in enumerate(INPUT_LINES):
            screen.addstr(i, 0, (JACK_FORMAT % (i+1)) + ': ' + str(ADC.read(input_line)))
        screen.addstr(len(INPUT_LINES)+1, 0, 'Hit "%s" to quit: ' % EXIT_KEY_NAME)

        screen.refresh()
        curses.napms(100)

    curses.endwin()
