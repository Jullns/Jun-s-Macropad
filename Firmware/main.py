import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D2, board.D3)
keyboard.row_pins = (board.D4, board.D5, board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

holdtap = HoldTap()
encoder_handler = EncoderHandler()
keyboard.modules = [holdtap, encoder_handler]

encoder_handler.pins = ((board.D1, board.D0, board.D10),)
encoder_handler.map = [(
    (KC.LCTRL(KC.EQUAL), KC.LCTRL(KC.MINUS)),
    KC.MUTE,
)]

holdtap.tap_time = 200

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
    ]
]

if __name__ == '__main__':
    keyboard.go()
