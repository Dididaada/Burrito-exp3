#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# importing user units
import functions as f


# Create your objects here.
EV3 = EV3Brick()

# timer
T = StopWatch()

# marche motors
R = Motor(Port.C)  #right wheel
L = Motor(Port.B)  #left wheel

# grabbing motors
CLAW = Motor(Port.A)
LIFT = Motor(Port.D)

# initialize sensor
RCOLOR = ColorSensor(Port.S3)
LCOLOR = ColorSensor(Port.S2)
G = GyroSensor(Port.S4)
BCOLOR = ColorSensor(Port.S1)

f.beep(EV3)


# Write your program here.

f.startup_sound(EV3)

#1 jump 10 centimeters straight-out without caring of crossing line ++
#2 line-follow to the Г-shaped crossing  ++
# f.lineFollowToGamma(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R) 
#3 turn 90 degrees right
#4 * confirm it stays at line and reallign if needed
#5 line follows to + crossing 
#6 line follows to next + crossing 
#7 turn 90 degrees left

f.turn90Left(EV3,G,L,R):

#8 reallign with + by going 720 degrees back and then forward until + in sight
#9 from this place keep gyro following N centimeters straight
#10 45degree to the left
#11 grab left brick



# drive to the next threshold
#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R)

#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R)