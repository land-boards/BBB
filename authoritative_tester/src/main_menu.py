from app_config import *
from menu import Menu
import curses

class MainMenu(Menu):
    def __init__(self, screen, options):
        Menu.__init__(self, screen)
        self.options = options
        self.highlight_index = 0

    def show_text(self):
        self.if_enter_show_option()
        self.update_highlighted_if_necessary()
        self.draw_options()

        self.show_quit(self.len_options()+1)

    def delay(self):
        return MENU_DELAY_MS

    def draw_options(self):
        for i, option in enumerate(self.options):
            self.screen.addstr(i, 0, option, (curses.A_DIM if i != self.highlight_index else curses.A_REVERSE))

    def if_enter_show_option(self):
        if self.key_pressed == 67:
            menu = self.build_current_menu()
            menu.set_parent(self)
            menu.show()

    def update_highlighted_if_necessary(self):
        if self.key_pressed == 65:
            self.highlight_index = (self.highlight_index - 1) % self.len_options()
        if self.key_pressed == 66:
            self.highlight_index = (self.highlight_index + 1) % self.len_options()

    def build_current_menu(self):
        return self.options[self.options.keys()[self.highlight_index]]()

    def len_options(self):
        return len(self.options)
