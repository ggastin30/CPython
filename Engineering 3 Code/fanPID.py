import time
import digitalio
import board
from PID_CPY import PID
import simpleio
import analogio
# Import necessary libraries

pid = PID(1, 0, 0, setpoint=1000, sample_time=0.01)
pid.output_limits = (None, None)    # Output value will be between 

photoI = digitalio.DigitalInOut(board.D8)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP
# Set up digital input for photo interrupter and enable its pull-up resist

Fan = analogio.AnalogOut(board.A1)

last_I = 0
new_I = 0
since_I = 0
State = 1
rpm = 0
pidReturn = 1200


while True:

    Fan.value = int(simpleio.map_range(pidReturn, -1200, 1200, 0, 65000))
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
            pidReturn = rpm + output
            print((rpm, output, pidReturn))
            time.sleep(.05)
            State = 1
    