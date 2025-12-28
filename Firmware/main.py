import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
macros = Macros()
encoder_handler = EncoderHandler()

keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)

PINS = [
    board.D0, board.D1, board.D2, board.D3, 
    board.D4, board.D5, board.D6, board.D10,
    board.D7
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder_handler.pins = (
    (board.D8, board.D9, None, False),
)

keyboard.keymap = [
    [
        KC.ESC,
        KC.HT(KC.DEL, KC.X),
        KC.HT(KC.LSFT, KC.Z),
        KC.HT(KC.M, KC.Y),
        KC.HT(KC.W, KC.Y),
        KC.HT(KC.LCTRL, KC.C),
        KC.HT(KC.A, KC.C),
        KC.HT(KC.D, KC.V),
        KC.MUTE,
    ]
]

encoder_handler.map = [
    ( (KC.MW_UP, KC.MW_DN), )
]

if __name__ == '__main__':
    keyboard.go()
