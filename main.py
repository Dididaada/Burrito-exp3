# Alex version of main.py (works)
#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
import functions as f

# Initialize the EV3 brick.
ev3 = EV3Brick()
ev3.screen.print("STARTED")
wait(3000)
ev3.screen.clear()

# Define and initialize the motors and color sensors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_color_sensor = ColorSensor(Port.S4)
right_color_sensor = ColorSensor(Port.S1)

# Define color thresholds for black+6, white, and blue lines.
BLACK_THRESHOLD_L = 30
BLACK_THRESHOLD_R = 30
WHITE_THRESHOLD_L = 300
WHITE_THRESHOLD_R = 300
BLUE_THRESHOLD = 150  # Adjust this threshold based on sensor readings.

# PID constants (adjust as needed).
KP = 1.0  # Proportional gain
KI = 0.05  # Integral gain
KD = 0.0  # Derivative gain

# Anti-windup parameters.
MAX_INTEGRAL = 1000  # Maximum allowable integral term value.
MIN_INTEGRAL = -1000  # Minimum allowable integral term value.

# Speed for slow movement and speed increment.
SLOW_SPEED = 50  # Adjust this value for your robot.
SPEED_INCREMENT = 5  # Adjust this value for smaller steps.

# Call the function to start line following with PID control.
f.line_following_pid(ev3, left_motor, right_motor, left_color_sensor, right_color_sensor,
                     BLACK_THRESHOLD_L, BLACK_THRESHOLD_R, WHITE_THRESHOLD_L, WHITE_THRESHOLD_R,
                     BLUE_THRESHOLD, KP, KI, KD, MAX_INTEGRAL, MIN_INTEGRAL, SLOW_SPEED, SPEED_INCREMENT)
                     

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
