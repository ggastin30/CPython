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
##### The goal of this assignment was to get started on some basic circuit python code and make the neopixel flash a red light.

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

### Wiring
There is no wiring needed because the neopixel is part of the board. 

### Reflection
 Importing things is very important. You can only use functions that are first imported and the files are put in the lib folder. 
 Unlike Arduino, the loop for circuit python is the "while true:" instead of void loop. 
 You need to check the serial monitor of the board to see if anything is wrong. The serial monitor on the computer is not as useful.

## Servo
####


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)


## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
