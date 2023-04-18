import time
import digitalio
import board

#Import necessary libraries

photoI = digitalio.DigitalInOut(board.D8)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP

#Set up a digital input for the photo interrupter and enable its pull-up resistor

last_photoI = True

interrupts = 0

while True:
    if photoI.value == True & last_photoI == True:
        interrupts = interrupts + 1
        last_photoI = False
    if last_photoI == False:
        time.sleep(.01)
        last_photoI = True
    print(interrupts)
    time.sleep(.001)