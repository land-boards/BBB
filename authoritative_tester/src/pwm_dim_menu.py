from menu import Menu
from app_config import *
import Adafruit_BBIO.PWM as PWM
import curses

class PwmDimMenu(Menu):
    def __init__(self, screen, jack_to_pwm):
        Menu.__init__(self, screen)
        self.jack_to_pwm = jack_to_pwm
        self.jacks = self.jacks_to_pwm.keys()
        self.pwm_index = 0

    def show_text(self):
        self.show_menu()

        self.dim_current_and_move_next()

    def dim_current_and_move_next(self):
        duty_cycle = 0.0
        PWM.start(self.current_pwm(), duty_cycle, 1000, 1)

        while duty_cycle <= 100.0:
            PWM.set_duty_cycle(self.current_pwm(), duty_cycle)
            curses.napms(DIM_DELAY_MS)
            duty_cycle += 0.5

        PWM.stop(self.current_pwm())
        self.move_next()

    def current_pwm(self):
        return self.jack_to_pwm[self.jacks[self.pwm_index]]

    def move_next(self):
        self.pwm_index = (self.pwm_index + 1) % len(self.jacks)

    def show_menu(self):
        self.screen.addstr("Dimming!")
        self.show_quit(2)
        self.screen.refresh()

    def delay(self):
        return 0
