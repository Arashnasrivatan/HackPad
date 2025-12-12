from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digitalio import MatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.handlers.sequences import send_string
from kmk.keys import KC

from kmk.extensions.neopixel import NeoPixel
import board
keyboard = KMKKeyboard()

pixels = NeoPixel(
    pin=board.GP2,
    num_pixels=2,
    brightness=0.2,
)

keyboard.matrix = MatrixScanner(
    col_pins=[],
    row_pins=[
        board.A0,  # SW1
        board.A1,  # SW2
        board.A2,  # SW3
        board.A3,  # SW4
        board.GP6, # SW5
        board.GP7, # SW6
    ],
    max_events=6,
)

encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = ((board.GP0, board.GP1, board.GP3),)

encoder.map = [
    ((KC.VOLU,), (KC.VOLD,)),
]

ENC_BTN = KC.ENT
ALT_TAB   = KC.LALT(KC.TAB)
CTRL_TAB  = KC.LCTRL(KC.TAB)
ALT_F4    = KC.LALT(KC.F4)
CUSTOM    = KC.LCTRL(KC.LSHIFT(KC.ESC))

keyboard.keymap = [
    [
        ALT_TAB,  # SW1
        CTRL_TAB, # SW2
        ALT_F4,   # SW3
        CUSTOM,   # SW4
        KC.A,     # SW5
        KC.B,     # SW6
    ]
]
def update_leds():
    pixels.fill((0, 50, 150))

update_leds()

if __name__ == '__main__':
    keyboard.go()
