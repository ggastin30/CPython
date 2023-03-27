# Circuit Python
This README contains documentation of my experiences through the new and foreign world of circuit python. If you are going to borrow some of it, please give credit or else you have plagiarised. See other people in my class at: (https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_DistanceSensor](#CircuitPython_DistanceSensor)
* [CircuitPython_LCD](#CircuitPython_LCD)

---
## Hello_CircuitPython

### Code
``` python
#Grant Gastinger
#firstAssignment
#Turns the neopixel red and makes it blink
#Code Based of Example code from Engineering 3 Canvas

from time import time
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #sets the pin for the neopixel
dot.brightness = 0.5 

print("Make it red!")

while True:
dot.fill((255, 0, 0)) #turns neopixel red
time.sleep(0.5) #pause 1/2 second
dot.fill((0,0,0)) #turn neopixel off
time.sleep(0.5)
```
### Evidence
https://user-images.githubusercontent.com/91094422/192555526-bd92a678-54f8-4581-986d-d5b9983d4272.mp4

### Wiring
There is no wiring needed because the neopixel is part of the board. 

### Reflection
* Importing things is very important. You can only use functions that are first imported and the files are put in the lib folder. 
* Unlike Arduino, the loop for circuit python is the "while true:" instead of void loop. 
* You need to check the serial monitor of the board to see if anything is wrong. The serial monitor on the computer is not as useful.
 
 ---

## CircuitPython_Servo

### Code

``` python
#Grant Gastinger
#servoAssignment
#Makes a 180 servo turn back and forth 
#Based off of code from: 2018 Kattni Rembor for Adafruit Industries

import time
import board
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=250) # create a PWMOut object on Pin A2.

my_servo = servo.Servo(pwm) # Create a servo object, my_servo.

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle #slowly changes angle by 5 degrees
        time.sleep(0.01)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.01)

```

### Evidence
https://user-images.githubusercontent.com/91094422/193044111-5d46a9d9-b366-4e6e-9d3c-922e085cacc6.mp4

### Wiring
![EliasWiring](https://user-images.githubusercontent.com/91094422/193046672-c67778a8-b683-4d67-8af1-8846cccd1db1.png)

Image credit: [Elias Garcia](https://github.com/egarcia28/CircuitPython)

### Reflection
[Here's where I found the basis for my code](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo)  There was one issue, you need to use the D pins(digital pins) for the servo, not the A pins.

---

## CircuitPython_DistanceSensor

### Code

``` python
#Grant Gastinger
#ultraSensor
#Have a neopixel fade colors from green to blue to red when at <5cm, 5-20cm, >20cm
#Based off code from Graham Gilbert-Schroeer
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Mason = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code, Mason = the neopixel
Mason.brightness = .5  #setting the brightness of the light, from 0-1 brightness
red = 0
blue = 0
green = 0

while True: #void loop
    try:
        cm = sonar.distance #measure sonar distance in cm
        print((sonar.distance))
        time.sleep(0.01)
        if cm < 5:
            Mason.fill((255, 0, 0))#red
        if cm > 5 and cm < 12.5: #fade red to blue at this interval
            red = simpleio.map_range(cm,5,12.5,255,0)
            blue = simpleio.map_range(cm,5,12.5,0,255)
            Mason.fill((red, 0, blue))
        if cm > 12.5 and cm < 20: #Blue to green at this interval
            blue = simpleio.map_range(cm,12.5,20,255,0)
            green = simpleio.map_range(cm,12.5,20,0,255)
            Mason.fill((0, green, blue))
        if cm > 20:
            Mason.fill((0, 255, 0))#green
    except RuntimeError: #If it doesn't work, try again
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence
https://user-images.githubusercontent.com/91094422/193284908-be352a88-619a-47df-9850-289edfa8f144.mp4

### Wiring
![eLIAS3](https://user-images.githubusercontent.com/91094422/193285420-b9590fd5-7f85-4ac5-8543-de44b9a417bd.png)

Image Credit: [Elias Garcia](https://github.com/egarcia28/CircuitPython)

### Reflection
When dealing with if statements, instead of using brackets like in arduino, you need to make sure the code is indented correctly. If a line of code is not indented enough, it will not be run in the loop. The syntax for the map function is "variable = simpleio.map_range(measured variable, input min, input max, output min, output max). "try" is a loop that checks a bunch of if statements and if none of them work, it runs the "except RuntimeError:" loop. 

## CircuitPython_TMP36

### Code

``` python
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
```

### Evidence
https://user-images.githubusercontent.com/91094422/227958939-2c2409b1-4215-4c89-82d6-b5a4610543a1.mp4

### Wiring
![image](https://user-images.githubusercontent.com/91094422/227959484-2b4946bd-25eb-40a5-8cdf-d9cb118c32d0.png)

Image Credit: [Sophie Chen](https://github.com/sechen12/CircutPython)

### Reflection

