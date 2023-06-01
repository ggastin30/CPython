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

sP = 700 #set point

pid = PID(12.5, .25, 2.5, setpoint=sP, sample_time=0.01) #D generally dampens oscillations previously 6,.1,2.5
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
Enstate = 700

Fan = analogio.AnalogOut(board.A1)

lcdPower = digitalio.DigitalInOut(board.D9) #connects the lcd to pin 9
lcdPower.direction = digitalio.Direction.INPUT #sets the lcd power flow as input
lcdPower.pull = digitalio.Pull.DOWN #Pulls the power of the lcd down to ground
while lcdPower.value is False: #creates an infinite loop that repeats until the lcd turns on
    print("zzz")
    time.sleep(0.1)
print("I'm awake")
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


last_I = 0
new_I = 0
since_I = 0
State = 0
rpm = 0
output = sP
oldTime = time.monotonic()
G = 0 #Debounce Variable



while True:
    while State == 0:
        Fan.value = int(simpleio.map_range(output, 0, 1200, 27500, 29000))
        #Fan.value = 28750 #27500(300) - 28750(1100)
        if btn.value == False:
            time.sleep(.5)
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("MENU MODE       ")
            State = 4
            break
        #print(btn.value)
        if time.monotonic() > oldTime +.1:
            lcd.set_cursor_pos(0, 0)
            lcd.print("PID MODE        ")
            State = 1
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
        output = pid(rpm)
        RPM = int(rpm)
        lcd.set_cursor_pos(1, 0)
        lcd.print("RPM:" + str(RPM) + " Set:" + str(sP))
        print((rpm, rpm, sP))
        # lcd.print(rpm)
        oldTime = time.monotonic()
        State = 0
    while State == 4: #Menu/PID selection
        position = encoder.position
        if position != last_position:
            if (position > last_position) & (G == 0):
                if Enstate > 500:
                    Enstate = Enstate - 10
                lcd.set_cursor_pos(1, 0)
                lcd.print("ChangeSet: " + str(Enstate))
                G = 1
                last_position = position
            elif (position < last_position) & (G == 0):
                if Enstate < 1100:
                    Enstate = Enstate + 10
                lcd.set_cursor_pos(1, 0)
                lcd.print("ChangeSet: " + str(Enstate))
                G = 1
                last_position = position
            G = 0
        Fan.value = 27500
        #print(btn.value)
        if btn.value == False:
            time.sleep(.5)
            sP = Enstate
            pid.setpoint = sP
            lcd.clear()
            State = 1
