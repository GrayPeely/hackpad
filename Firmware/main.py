print("Starting")

import board

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

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
