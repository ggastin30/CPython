# CPython
(https://github.com/chssigma/Class_Accounts).
## Blink Red
##### The goal of this assignment was to get started on some basic circuit python code and make the neopixel flash a red light.

### Description & Code
```
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

### Wiring
There is no wiring needed because the neopixel is part of the board. 

## Reflection
 Importing things is very important. You can only use functions that are first imported and the files are put in the lib folder. 
 Unlike Arduino, the loop for circuit python is the "while true:" instead of void loop. 
 You need to check the serial monitor of the board to see if anything is wrong. The serial monitor on the computer is not as useful.


## Hello_CircuitPython


Description goes here




### Evidence
![iCanDoGifs](https://github.com/mtimmin65/circuitpython/blob/main/ledgif.gif?raw=true)


### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

```python
"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence

<img src="WIN-20210917-15-19-55-Pro (2).gif" alt="servodemo" width="500">

### Wiring

### Reflection




## CircuitPython_LCD

This assignment was to make it so the distance on the ultrasonic sensor corresponds with the color displayed on the Metro board.

```python
import adafruit_hcsr04
import time
import board
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = 0.1

while True:
    try:
        dist = sonar.distance
        print((dist))
        r = max(min(15*(20-dist),255),0)
        g = max(min(15*(dist-20),255),0)
        b = max(min(-abs(15*(20-dist))+225,255),0)
        dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence
     
<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/IMG-86812912-3 (1).gif?raw=true" alt="CircuitPython_LCD" width="500">
     
### Wiring

<img src="https://github.com/ezell38/Hello_CircuitPython/blob/main/Images/Capture.1.PNG?raw=true" alt="CircuitPythonDistance" width="500">
Capture.1.PNG

### Reflection

This assignment was hard because I kept saving the code to a file on my computer and not my Metro board. I also used some code from another student and didn't adjust my wiring to fit their code which messed up my Ultrasonic sensor. 




## photo resistor 

### Description & Code

```python
from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.time() + 4
        counter = 0

```

### Evidence


<img src="https://github.com/mtimmin65/circuitpython/blob/main/ezgif-3-777ed7b0fb7c.gif?raw=true" alt="Italian Trulli">
### Wiring

### Reflection
