import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import analogio
import digitalio
import rotaryio

lcdPower = digitalio.DigitalInOut(board.D8)
lcdPower.direction = digitalio.Direction.INPUT
lcdPower.pull = digitalio.Pull.DOWN

while lcdPower.value is False:
    print("zzz")
    time.sleep(0.1)

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
lcd.print("Hello World")

btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

encoder = rotaryio.IncrementalEncoder(board.D10, board.D9)
last_position = None 

while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position