# Blink Red
##### The goal of this assignment was to get started on some basic circuit python code and make the neopixel flash a red light.

### Code
```
from time import time
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
dot.fill((255, 0, 0))
time.sleep(0.5)
dot.fill((0,0,0))
time.sleep(0.5)
```

### Wiring
There is no wiring needed because the neopixel is attached to the board. 

## Reflection
Importing things is very important. You can only use functions that are first imported and the files are put in the lib folder.
