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

sP = 800

pid = PID(5, .1, 2.5, setpoint=sP, sample_time=0.01) #D generally dampens oscillations 
pid.output_limits = (None, None)    # Output value will be between 

photoI = digitalio.DigitalInOut(board.D8)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP
# Set up digital input for photo interrupter and enable its pull-up resist

Fan = analogio.AnalogOut(board.A1)

# i2c = board.I2C()
# lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

# encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)
# last_position = 0
# btn = DigitalInOut(board.D1)
# Vbtn.direction = Direction.INPUT
# btn.pull = Pull.UP
# Enstate = 0

last_I = 0
new_I = 0
since_I = 0
State = 1
rpm = 0
output = sP


while True:
    # position = encoder.position
    # if position != last_position:
    #    if position > last_position:
    #       Enstate = Enstate + 1
    #   elif position < last_position:
    #       Enstate = Enstate - 1
    Fan.value = int(simpleio.map_range(output, 0, sP, 0, 65000))
    while State == 1:  # first trigger
        if photoI.value is True:  # if triggered
            last_I = time.monotonic()
            time.sleep(.05)
            State = 2
    while State == 2:  # second trigger
        if photoI.value is True:  # if triggered
                new_I = time.monotonic()
                State = 3
    while State == 3:  # computation
            since_I = new_I - last_I
            rpm = 60/since_I
            #print((rpm, rpm, rpm))  
            output = pid(rpm)
            print((rpm, output, sP))
            # lcd.print(rpm)
            time.sleep(.05)
            State = 1
    