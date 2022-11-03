
import board
import simpleio
from analogio import AnalogIn
from adafruit_motor import motor


potentiometer = AnalogIn(board.A0)
motor1 = motor.DCMotor(board.D6)

print("hello world")

while True:
    print((potentiometer.value,)) 
    ticks = potentiometer.value
    speed = simpleio.map_range(ticks,0,1023,0,1)
    motor1._throttle(str(speed))