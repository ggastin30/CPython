import board
import time
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:
    if not btn.value:
        #lcd.clear()
        #lcd.set_cursor_pos(0, 0)
        #lcd.print("Button Pressed")
        print("Button Pressed")
    else:
        print("press me")
        pass
    time.sleep(0.1) # sleep for debounce
