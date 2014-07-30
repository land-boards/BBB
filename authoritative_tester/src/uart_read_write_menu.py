from menu import Menu
from app_config import *
import Adafruit_BBIO.UART as UART
import curses
import serial

class UartReadWriteMenu(Menu):
    def __init__(self, screen, tx_to_rx):
        Menu.__init__(self, screen)
        self.tx_to_rx = tx_to_rx
        self.txs = self.tx_to_rx.keys()
        self.uart_index = 0
        self.setup_uarts()

    def show_text(self):
        self.show_menu()

        ser_out = serial.Serial(port = self.uart_to_device(self.current_tx()), baudrate = 9600)
        ser_out.close()
        ser_out.open()
        if ser_out.isOpen():
            ser_out.write("Hello World!")
        ser_out.close()

        ser_in = serial.Serial(port = self.uart_to_device(self.current_rx()), baudrate = 9600)
        ser_in.close()
        ser_in.open()
        if ser_in.isOpen():
            ser_in.readline(0.1)
        ser_in.close()

        self.move_next()

    def setup_uarts(self):
        uarts_to_setup = set([i for i in self.tx_to_rx.keys()] + [i for i in self.tx_to_rx.values()])
        for uart in uarts_to_setup:
            UART.setup(uart)

    def uart_to_device(self, uart):
        return '/dev/ttyO' + uart[-1]

    def current_tx(self):
        return self.txs[self.uart_index]

    def current_rx(self):
        return self.tx_to_rx[self.current_tx()]

    def move_next(self):
        self.uart_index = (self.uart_index + 1) % len(self.tx_to_rx)

    def show_menu(self):
        self.screen.addstr(self.current_tx() + ' -> ' + self.current_rx())
        self.show_quit(2)
        self.screen.refresh()

    def delay(self):
        return 100
