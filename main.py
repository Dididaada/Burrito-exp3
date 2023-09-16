#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

"""Initialization of everything"""
import functions as f
# brick
EV3 = EV3Brick()

# timer
t = StopWatch()

# marche motors
RM = Motor(Port.C)
LM = Motor(Port.B)


# initialize sensor
CR = ColorSensor(Port.S1)
CL = ColorSensor(Port.S4)
G = GyroSensor(Port.S3)


""" START """ 
#ev3.speaker.beep()



""" MAIN SEQUENCE """
start=t.time()



# jump over the front line
"""
start_angle=G.angle()
RM.run(-500)
LM.run(-500)
wait(1000)
"""

#1 jump 10 centimeters straight-out without caring of crossing line ++
#2 line-follow to the Г-shaped crossing  ++
# f.lineFollowToGamma(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R) 
#3 turn 90 degrees right
f.turn180(EV3,LM,RM,G)
#4 * confirm it stays at line and reallign if needed
#5 line follows to + crossing 
#6 line follows to next + crossing 
#7 turn 90 degrees left
#8 reallign with + by going 720 degrees back and then forward until + in sight
#9 from this place keep gyro following N centimeters straight
#10 45degree to the left
#11 grab left brick



"""
start_angle=G.angle()
RM.run(500)
LM.run(-500)
while(True):
    if G.angle()-start_angle>=80:
        ev3.screen.print("RIGHT turn DONE")
        break
RM.stop()
LM.stop()
"""



""" END OF WORK """


EV3.speaker.play_notes(["G4/8","E4/8","C4/8"], tempo=120)
wait(5000)
