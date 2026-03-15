print("Starting")

import board
import busio

from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros


keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D6, board.D7, board.D8, board.D9]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#Test values for now.
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

#oled testing
i2c = busio.I2C(board.SCL, board.SDA)

display = Display(
    display=SSD1306()
    entries=[
        TextEntry(text='Olo Test 123'),
    ],
)

keyboard.extensions.append(display)

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
