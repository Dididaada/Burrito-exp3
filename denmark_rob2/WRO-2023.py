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
CLAW = Motor(Port.A) #Motor(Port.A)
LIFT = Motor(Port.D) #Motor(Port.D)

# initialize sensor
RCOLOR = ColorSensor(Port.S1) 
LCOLOR = ColorSensor(Port.S4)
G = GyroSensor(Port.S3)
FCOLOR = ColorSensor(Port.S2)
BCOLOR = ""
# Store the initial angle before the 15-degree turn
initial_angle = G.angle()



f.startupSound(EV3) 


#pickupFromSense(EV3,G,L,R,CLAW,LIFT)


#1 display data
f.print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
wait(500)
f.liftForkUp(EV3, LIFT)
wait(500)

"""
#2 jump forward 1000ms
L.run(-80)
R.run(-80)
wait(4000)
R.stop()
L.stop()
"""
f.prepareToTakeObject(EV3, LIFT)
f.open(EV3, CLAW)

"""
#3 proceed to the next threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

R.run(-150)
L.run(-150)
wait(3500)
R.stop()
L.stop()
"""
f.close(EV3, CLAW)

f.putObjectTo80Degrees(EV3, LIFT)
"""
#4 step forward - push the ship
R.run(80)
L.run(80)
"""
f.putRedOnback(EV3, CLAW)
f.open(EV3, CLAW)
f.putObjectTo80Degrees(EV3, LIFT)
"""
wait(7000)
f.turnTo45(EV3,G,L,R)
wait(500)

#3.* lil forward
f.forward(EV3,L,R,T,100)
#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
f.turnTo90(EV3, G, L, R)
f.beep(EV3)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"Starting sec1")
wait(500)
L.stop()
R.stop()
f.forward(EV3, L, R,T,2000)
f.beep(EV3)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"Starting sec2")
f.forward(EV3, L, R,T,2000)
f.beep(EV3)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"Starting sec3")
wait(500)
f.turnTodegree(EV3,G,L,R, 10)

L.run(-120)
R.run(-80)
wait(8000)
R.stop()
L.stop()

f.beep(EV3)
"""
"""

f.turnTo45(EV3,G,L,R)
wait(1000)

#3.* lil forward
f.forward(EV3,L,R,T,100)
#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

#4 turn right 90 degrees
f.turnTo90(EV3,G,L,R)
wait(1000)

#5 proceed to the next threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
R.run(-80)
L.run(-80)
wait(2000)
#6 proceed to the next threshold



f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

#7 turning north
f.turnTo0(EV3,G,L,R)
wait(1000)

CLAW.dc(50)  # Adjust the speed as needed

CLAW.stop(Stop.BRAKE)

#8 Stop if the front sensor detects anything more than 0 in RGB and rotate towards the block 
f.tothethresholdsinglecase(EV3,LCOLOR,FCOLOR,RCOLOR,G,L,R,T)

"""
"""
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
CLAW = Motor(Port.A) #Motor(Port.A)
LIFT = Motor(Port.D) #Motor(Port.D)

# initialize sensor
RCOLOR = ColorSensor(Port.S1) 
LCOLOR = ColorSensor(Port.S4)
G = GyroSensor(Port.S3)
FCOLOR = ColorSensor(Port.S2)
BCOLOR = ""
# Store the initial angle before the 15-degree turn
initial_angle = G.angle()



f.startupSound(EV3) 


#pickupFromSense(EV3,G,L,R,CLAW,LIFT)


#1 display data
f.print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
wait(500)
f.liftForkUp(EV3, LIFT)
wait(500)


#2 jump forward 1000ms
L.run(-80)
R.run(-80)
wait(4000)
R.stop()
L.stop()

f.prepareToTakeObject(EV3, LIFT)
f.open(EV3, CLAW)


#3 proceed to the next threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

R.run(-150)
L.run(-150)
wait(3500)
R.stop()
L.stop()

f.close(EV3, CLAW)

f.putObjectTo80Degrees(EV3, LIFT)

#4 step forward - push the ship
R.run(80)
L.run(80)

wait(7000)
f.turnTo45(EV3,G,L,R)
wait(500)

#3.* lil forward
f.forward(EV3,L,R,T,100)
#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
f.turnTo90(EV3, G, L, R)
f.beep(EV3)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"Starting sec1")
wait(500)
L.stop()
R.stop()
f.forward(EV3, L, R,T,2000)
f.beep(EV3)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"Starting sec2")
f.forward(EV3, L, R,T,2000)
f.beep(EV3)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"Starting sec3")
wait(500)
f.turnTodegree(EV3,G,L,R, 10)

L.run(-120)
R.run(-80)
wait(8000)
R.stop()
L.stop()

f.beep(EV3)
"""

"""

f.turnTo45(EV3,G,L,R)
wait(1000)

#3.* lil forward
f.forward(EV3,L,R,T,100)
#f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

#4 turn right 90 degrees
f.turnTo90(EV3,G,L,R)
wait(1000)

#5 proceed to the next threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
R.run(-80)
L.run(-80)
wait(2000)
#6 proceed to the next threshold



f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

#7 turning north
f.turnTo0(EV3,G,L,R)
wait(1000)

CLAW.dc(50)  # Adjust the speed as needed

CLAW.stop(Stop.BRAKE)

#8 Stop if the front sensor detects anything more than 0 in RGB and rotate towards the block 
f.tothethresholdsinglecase(EV3,LCOLOR,FCOLOR,RCOLOR,G,L,R,T)

"""
