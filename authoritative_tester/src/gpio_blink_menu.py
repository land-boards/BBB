from menu import Menu
from app_config import *
import Adafruit_BBIO.GPIO as GPIO
import curses

class GpioBlinkMenu(Menu):
    def __init__(self, screen, jack_to_gpio):
        Menu.__init__(self, screen)
        self.jack_to_gpio = jack_to_gpio
        for gpio in self.jack_to_gpio.values():
            GPIO.setup(gpio, GPIO.OUT)

        self.light_is_on = False
        self.jacks = sorted(self.jack_number(j) for j in self.jack_to_gpio.keys())
        self.jack_index = 0

    def show_text(self):
        self.show_menu()

        self.blink_current_and_move_next()

    def current_gpio(self):
        return self.jack_to_gpio[self.current_jack_name()]

    def blink_current_and_move_next(self):
        GPIO.output(self.current_gpio(), GPIO.HIGH)
        curses.napms(BLINK_DELAY_MS)
        GPIO.output(self.current_gpio(), GPIO.LOW)

        self.move_next()

    def show_menu(self):
        self.screen.addstr("Cycling between LEDs!")
        self.show_quit(2)
        self.screen.refresh()

    def jack_number(self, jack):
        return int(jack[1:])

    def current_jack_name(self):
        return 'J' + str(self.jacks[self.jack_index])

    def move_next(self):
        self.jack_index = (self.jack_index + 1) % len(self.jacks)

    def delay(self):
        return 0
