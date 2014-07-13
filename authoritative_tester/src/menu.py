from app_config import *
import curses

class Menu(object):
    def __init__(self, screen):
        self.screen = screen
        self.key_pressed = 0

    def show(self):
        try:
            while self.key_pressed != ord(QUIT_CHARACTER):
                self.screen.clear()
                self.key_pressed = self.screen.getch()

                self.show_text()

                self.screen.refresh()
                curses.napms(self.delay())
        finally:
            curses.endwin()

    def show_quit(self, index):
        self.screen.addstr(index, 0, 'Hit "%s" to quit' % QUIT_CHARACTER)

    def set_parent(self, parent):
        self.main_menu = parent

    def delay(self):
        return MENU_DELAY_MS

    def show_text(self):
        raise NotImplementedError('Base classes must implement show_text')
