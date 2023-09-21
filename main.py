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

f.beep(EV3)

f.startupSound(EV3)


# 0 display data
f.print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
wait(1000)
# 1 go forward and proceed to the next threshold
f.forward(EV3,L,R,T,2000)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
# 2 go back
f.backward(EV3,L,R,T,1600)
f.beep_if_gyro_not_zero(EV3, G)
# 3 turn right 45 degrees 
f.turnTo45(EV3,G,L,R)
wait(1000)
# 4 go forward 
f.forward(EV3,L,R,T,1000)
# 5 turn 90, it gets back on the line and continues to follow the line
f.turnTo90(EV3,G,L,R)
wait(1000)
# 6 reach the 2d cross 
    # proceed to the next threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
    # proceed to the next threshold
f.forward(EV3,L,R,T,2000)
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
# 7 turn north
f.turnTo0(EV3,G,L,R)
wait(1000)
# 8 stop if the front sensor detects anything more than 0 in RGB and rotate towards the block
f.forward(EV3,L,R,T, 2900) 
if f.deetectFront(EV3, FCOLOR) == "some col other than black":
    L.stop() 
    R.stop()
    EV3.screen.print("Front sensor detected something!")
# 9 reach the block looking to the north (fix the angle)
f.turnTo15(EV3, G, L, R)
wait(1000) 
      #Rotate back to the initial angle
f.rotateToInitialAngle(EV3, G, L, R, initial_angle)

# 10 grab it and lift it 
# 11 turn south (180) and find the line 
f.turn180(EV3, L, R, G)
wait(1000)


# 12 turn right and use follow the line 
f.turnTo45(EV3,G,L,R)
wait(1000)
# 13 next cross 
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"") 
# Perform the 15-degree turn


#9 Grabbing mechanism  
#11 going to the cross section 
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")

#13 go to the next threshold 


#14 turn to the ship dropping line
f.turnTo45(EV3,G,L,R)
wait(1000)

#15 going in the front and stopping at some point parallel to the ship 
f.forward(EV3,L,R,T,1000)

#16 turning on the left 
f.turnTo90left(EV3,G,L,R)
wait(1000)

#17 going to the ships to put down the first block
f.forward(EV3,L,R,T)
if f.deetectFront(EV3, FCOLOR) == "some col other than black":
    L.stop() 
    R.stop()
    EV3.screen.print("Front sensor detected something!") # this code stays here until it's tested

#18 putting down mechanism 

#19 Coming back to 3 blocks and pick one 
#19/1 turning back 
f.turn180(EV3, L, R, G)
wait(1000)
#19/2 going back to the threshold
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
#19/3 driving to the right to the threshold 
f.turnTo45(EV3,G,L,R)
wait(1000)
#go to the cross section 
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
#19/4 turning on the left and planning on picking up second block
f.turnTo90left(EV3,G,L,R)
wait(1000)
#19/5 getting to another threshold 
f.driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
#19/6 turn to the left 
f.turnTo90left(EV3,G,L,R)
wait(1000)
#19/7 go in the front until robot arrives at the three blocks 
f.forward(EV3,L,R,T)
if f.deetectFront(EV3, FCOLOR) == "some col other than black":
    L.stop() 
    R.stop()
    EV3.screen.print("Front sensor detected something!")


#f.print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,"")
wait(5000)



"""
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
"""

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
