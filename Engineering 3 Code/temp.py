#ctrl alt r
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import analogio
import digitalio

lcdPower = digitalio.DigitalInOut(board.D8)
lcdPower.direction = digitalio.Direction.INPUT
lcdPower.pull = digitalio.Pull.DOWN

while lcdPower.value is False:
    print("zzz")
    time.sleep(0.1)


TMP36_PIN = board.A0  # Analog input connected to TMP36 output.
i2c = board.I2C()

# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)


# Loop forever.
while True:
    lcd.clear()
    lcd.print("Grant")
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(1.0)