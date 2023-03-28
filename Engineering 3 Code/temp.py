#ctrl alt r
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import analogio
import digitalio

lcdPower = digitalio.DigitalInOut(board.D8) #connects the lcd to pin 8
lcdPower.direction = digitalio.Direction.INPUT #sets the lcd power flow as input
lcdPower.pull = digitalio.Pull.DOWN #Pulls the power of the lcd down to ground

while lcdPower.value is False: #creates an infinite loop that repeats until the lcd turns on
    print("zzz")
    time.sleep(0.1)


TMP36_PIN = board.A3  # Analog input connected to TMP36 output.
i2c = board.I2C() #I2c on the lcd

# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 54000) #Standard: 65535
    return (millivolts - 500) / 10

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16) #sets the format of lcd
# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN) #Sets the temperature sensor to pin 3 input
print("I'm awake")

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    if temp_F > 78: #if it's over 78, say it's too hot
        lcd.clear()
        lcd.print("TOO HAWT")
        time.sleep(1.0)
    elif temp_F < 70: #if it's below 70, say it's cold
        lcd.clear()
        lcd.print("BRRRR")
        time.sleep(1.0)
    else: #if it's normal, say it's room temp
        lcd.clear()
        lcd.print("Room Temperature")
    #lcd.print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(1.0)