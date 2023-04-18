import time
import digitalio
import board

#Import necessary libraries

photoI = digitalio.DigitalInOut(board.D7)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP

#Set up a digital input for the photo interrupter and enable its pull-up resistor

last_photoI = True
last_update = -4

#Initialize variables for counting the number of times the photo interrupter is triggered

photoICrosses = 0

while True:
    if time.monotonic()-last_update > 4:
        print(f"The number of crosses is {photoICrosses}")
        last_update = time.monotonic()
    
    if last_photoI != photoI.value and not photoI.value:
        # Check if the photo interrupter state has changed and if it is currently interrupted
        photoICrosses += 1
        # Increment the count of photo interrupter crosses
    last_photoI = photoI.value