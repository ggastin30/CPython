import time
import digitalio
import board

#Import necessary libraries

photoI = digitalio.DigitalInOut(board.D8)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP

#Set up a digital input for the photo interrupter and enable its pull-up resistor

last_I = 0
new_I = 0
since_I = 0
State = 1
rpm = 0


while True:
    while State == 1: #first trigger
        if photoI.value == True: #if triggered
            last_I = time.monotonic()
            time.sleep(.05)
            State = 2
    while State == 2: #second trigger
        if photoI.value == True: #if triggered
                new_I = time.monotonic()
                State = 3

    while State == 3: #computation
            since_I = new_I - last_I
            rpm = 60/since_I
            print(rpm)
            time.sleep(.05)
            State = 1    