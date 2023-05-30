import time
import digitalio
import board
from PID_CPY import PID
import simpleio
import analogio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import rotaryio
# Import necessary libraries

sP = 800 #set point

pid = PID(6, .1, 2.5, setpoint=sP, sample_time=0.01) #D generally dampens oscillations 
pid.output_limits = (None, None)    # Output value will be between 

photoI = digitalio.DigitalInOut(board.D8)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP
# Set up digital input for photo interrupter and enable its pull-up resist

encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)
last_position = 0
btn = digitalio.DigitalInOut(board.D1)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP
Enstate = 0

Fan = analogio.AnalogOut(board.A1)

#i2c = board.I2C()
#lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

last_I = 0
new_I = 0
since_I = 0
State = 0
rpm = 0
output = sP
oldTime = time.monotonic()
counter = 0
G = 0



while True:
    while State == 0:
        Fan.value = int(simpleio.map_range(output, 0, sP, 0, 65000))
        if btn == False:
            time.sleep(1)
            print("bananaKumquat")
            State = 4
        #print(btn.value)
        if time.monotonic() > oldTime +.5:
            State = 1
        print(State)
    while State == 1:  # first trigger
        if photoI.value is True:  # if triggered
            last_I = time.monotonic()
            time.sleep(.05)
            print(State)
            State = 2
    while State == 2:  # second trigger
        if photoI.value is True:  # if triggered
            new_I = time.monotonic()
            print(State)
            State = 3
    while State == 3:  # computation
        since_I = new_I - last_I
        rpm = 60/since_I
        output = pid(rpm)
        print((rpm, output, sP))
        # lcd.print(rpm)
        oldTime = time.monotonic()
        print(State)
        State = 0
    while State == 4:
        print(State)
        position = encoder.position
        if position != last_position:
            if (position > last_position) & (G == 0):
                Enstate = Enstate - 10
                print(Enstate)
                G = 1
                last_position = position
            elif (position < last_position) & (G == 0):
                Enstate = Enstate + 10
                print(Enstate)
                G = 1
                last_position = position
            G = 0
        #print(btn.value)
        if btn == False:
            sP = Enstate
            State = 1