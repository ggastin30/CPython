# Circuit Python
This README contains documentation of my experiences through the new and foreign world of circuit python. If you are going to borrow some of it, please give credit or else you have plagiarised. See other people in my class at: (https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---
## Hello_CircuitPython

### Description & Code
```
#Grant Gastinger
#Hello_CircuitPython
#Turns the neopixel red and makes it blink
#Code Based of Example code from Engineering 3 Canvas

from time import time
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
dot.fill((255, 0, 0))
time.sleep(0.5)
dot.fill((0,0,0))
time.sleep(0.5)
```
### Evidence
https://user-images.githubusercontent.com/91094422/192555526-bd92a678-54f8-4581-986d-d5b9983d4272.mp4

### Wiring
There is no wiring needed because the neopixel is part of the board. 

### Reflection
 Importing things is very important. You can only use functions that are first imported and the files are put in the lib folder. 
 Unlike Arduino, the loop for circuit python is the "while true:" instead of void loop. 
 You need to check the serial monitor of the board to see if anything is wrong. The serial monitor on the computer is not as useful.
 
 ---

## CircuitPython_Servo

### Description & Code

```
#Grant Gastinger
#CircuitPython_Servo
#Makes a 180 servo turn back and forth 
#Based off of code from: 2018 Kattni Rembor for Adafruit Industries

import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=250)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.01)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.01)

```

### Evidence
https://user-images.githubusercontent.com/91094422/193044111-5d46a9d9-b366-4e6e-9d3c-922e085cacc6.mp4

### Wiring
![EliasWiring](https://user-images.githubusercontent.com/91094422/193046672-c67778a8-b683-4d67-8af1-8846cccd1db1.png)

Image credit: Elias Garcia

### Reflection
[Here's where I found the basis for my code](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo)  There was one issue, you need to use the D pins(digital pins) for the servo, not the A pins.

---

## CircuitPython_DistanceSensor

### Description & Code

```
#Grant Gastinger
#CircuitPython_DistanceSensor
#Have a neopixel fade colors from green to blue to red when at <5cm, 5-20cm, >20cm
#Based off code from Graham Gilbert-Schroeer
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Mason = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Mason.brightness = .5  #setting the brightness of the light, from 0-1 brightness
red = 0
blue = 0
green = 0

while True:
    try:
        cm = sonar.distance
        print((sonar.distance))
        time.sleep(0.01)
        if cm < 5:
            Mason.fill((255, 0, 0))#red
        if cm > 5 and cm < 12.5:
            red = simpleio.map_range(cm,5,12.5,255,0)
            blue = simpleio.map_range(cm,5,12.5,0,255)
            Mason.fill((red, 0, blue))
        if cm > 12.5 and cm < 20:   
            blue = simpleio.map_range(cm,12.5,20,255,0)
            green = simpleio.map_range(cm,12.5,20,0,255)
            Mason.fill((0, green, blue))
        if cm > 20:
            Mason.fill((0, 255, 0))#green
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence

### Wiring

### Reflection
When dealing with if statements, instead of using brackets like in arduino, you need to make sure the code is indented correctly. If a line of code is not indented enough, it will not be run in the loop. The syntax for the map function is "variable = simpleio.map_range(measured variable, input min, input max, output min, output max). "try" is a loop that checks a bunch of if statements and if none of them work, it runs the "except RuntimeError:" loop. 

## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
