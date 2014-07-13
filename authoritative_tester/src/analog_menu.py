from menu import Menu
from app_config import *
import Adafruit_BBIO.ADC as ADC
import curses

class AnalogMenu(Menu):
    def __init__(self, screen, jack_to_analog):
        Menu.__init__(self, screen)
        self.jack_to_analog = jack_to_analog
        ADC.setup()

    def show_text(self):
        for i, jack in enumerate(self.sorted_jacks()):
            self.screen.addstr(i, 0, (jack) + ': ' + str(ADC.read(self.jack_to_analog[jack])))

        self.show_quit(len(self.jack_to_analog)+1)


    def sorted_jacks(self):
        numbers = sorted(int(j[1:]) for j in self.jack_to_analog.keys())
        return ['J' + str(n) for n in numbers]

    def delay(self):
        return ANALOG_MENU_DELAY_MS
