#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

# importing user units
import functions as f

# Create your objects here.
EV3 = EV3Brick()

# timer
T = StopWatch()

# screen font
small_font = Font(size=12)

# marche motors
R = Motor(Port.C)  #right wheel
L = Motor(Port.B)  #left wheel

# grabbing motors
CLAW = Motor(Port.A)
LIFT = Motor(Port.D)

# initialize sensor
RCOLOR = ColorSensor(Port.S1) 
LCOLOR = ColorSensor(Port.S4)
G = GyroSensor(Port.S3)
BCOLOR = ColorSensor(Port.S2)

f.beep(EV3)

f.startupSound(EV3)

#1 display data
f.print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
wait(1000)

#Debug
EV3.screen.print("starting debug")


EV3.screen.print(sum(BCOLOR.rgb()))
if sum(BCOLOR.rgb()) > 100:
    f.turn10right(EV3, L, R, G)
    f.pickAndLift(EV3,CLAW,LIFT)

#timesaver
while True:
    L.hold()
    R.hold()

#2 jump forward 1000ms
f.forward(EV3,L,R,T,2000)

#3 proceed to the next threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

#3.* lil back
f.backward(EV3,L,R,T,1200)

#4 turn right to 45 degrees
f.turnTo45(EV3,G,L,R)
wait(1000)

#3.* lil forward
f.forward(EV3,L,R,T,1000)

#4 turn right 90 degrees
f.turnTo45(EV3,G,L,R)
wait(1000)

#5 proceed to the next threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")


#6 proceed to the next threshold
f.forward(EV3,L,R,T,2000)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")


#7 turning north
f.turnTo0(EV3,G,L,R)
wait(1000)

#8 proceed to the next threshold
f.forward(EV3,L,R,T,2000)



#f.print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
wait(5000)



# Write your program here.


#1 jump 10 centimeters straight-out without caring of crossing line ++
#2 line-follow to the Г-shaped crossing  ++
# f.lineFollowToGamma(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R) 
#3 turn 90 degrees right
#4 * confirm it stays at line and reallign if needed
#5 line follows to + crossing 
#6 line follows to next + crossing 
#7 turn 90 degrees left
#8 reallign with + by going 720 degrees back and then forward until + in sight
#9 from this place keep gyro following N centimeters straight
#10 45degree to the left
#11 grab left brick



# drive to the next threshold
#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R)

#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R)
