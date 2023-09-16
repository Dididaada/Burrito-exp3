#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import brain

""" Initialization of everything """

# brick
ev3 = EV3Brick()

# timer
t = StopWatch()

# marche motors
RM = Motor(Port.D)
LM = Motor(Port.A)


# initialize sensor
CR = ColorSensor(Port.S1)
CL = ColorSensor(Port.S4)
G = GyroSensor(Port.S3)


""" START """ 
#ev3.speaker.beep()
brain.startup_sound(ev3)



""" MAIN SEQUENCE """
start=t.time()

"""
while(True):
    #brain.print_all_sensors(ev3,CL,CR,G)
    brain.print_rel(ev3,CL,CR)
    wait(2000)
    ev3.screen.clear()
"""
#1. front straight piece before the ship


# jump over the front line
start_angle=G.angle()
RM.run(-500)
LM.run(-500)
wait(1000)

# stop at the next threshold
while (True):
    if brain.follow_line(ev3,CL,CR)=="move on":
        ev3.screen.print("-==-")
        RM.run(-500)
        LM.run(-500)
    if brain.follow_line(ev3,CL,CR)=="turn left":
        ev3.screen.print("<-")
        RM.run(-500)
        LM.run(-400)
    if brain.follow_line(ev3,CL,CR)=="turn right":
        ev3.screen.print("->")
        RM.run(-400)
        LM.run(-500)
    if brain.follow_line(ev3,CL,CR)=="stop":
        ev3.screen.print("theshold")
        break
    if brain.follow_line(ev3,CL,CR)=="undefined":
        ev3.screen.print("undefined")
        break

#follow_line_until_crossing(ev3,CL,CR,G,LM,RM)
#follow_line_until_crossing(ev3,CL,CR,G,LM,RM)

# rotate 90 right
start_angle=G.angle()
RM.run(500)
LM.run(-500)
while(True):
    if G.angle()-start_angle>=80:
        ev3.screen.print("RIGHT turn DONE")
        break
RM.stop()
LM.stop()




""" END OF WORK """


ev3.speaker.play_notes(["G4/8","E4/8","C4/8"], tempo=120)
wait(5000)