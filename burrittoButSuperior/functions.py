from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

def detectColor(C):
    color = sum(C.rgb())
    if color >100: 
        #pure is 200
        return "white"
    if color <50:
        return "black"
    return "blue"

def _ContrSpeed():
    return -800

def _slow():
    return -80

def _slowBack():
    return 100

def _fast():
    return -250

def _fastBack():
    return 250


def beep(EV3):
    """
    Little beep  - a procedure
    Input: interface to EV3 brick
    """
    EV3.speaker.beep()

def startupSound(EV3):
    """
    sound imitating siren before mechanism started working
    """
    for j in range(3):
        for i in range(100,1000,40):
            EV3.speaker.beep(frequency=i, duration=7)


def displaySensors(EV3,LCOLOR,BCOLOR,RCOLOR,G):
    """
    prints on 
    """
def print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,message):
    EV3.screen.set_font(small_font)
    EV3.screen.clear() 
    EV3.screen.print("LEFT"+str(LCOLOR.rgb())+"\n"+str(sum(LCOLOR.rgb())))
    EV3.screen.print("RIGHT"+str(RCOLOR.rgb())+"\n"+str(sum(RCOLOR.rgb())))
    #EV3.screen.print("Side Sensor"+str(BCOLOR.rgb())+"\n"+str(sum(BCOLOR.rgb())))
    EV3.screen.print("Left+1  / right+1 =" + str((sum(LCOLOR.rgb())+1)   /  \
         (sum(RCOLOR.rgb())+1)))
    EV3.screen.print("Angle "+str(G.angle())+"º")
    EV3.screen.print("DEBUG MESSAGE "+message, end="")   

def open(EV3, CLAW):
    CLAW.run(300)

def followLine(EV3,LCOLOR,RCOLOR,BCOLOR,L,R):


    #EV3.screen.print(l+str(LCOLOR.rgb())+"==="+r+str(RCOLOR.rgb()))
    LEFT = detectColor(LCOLOR)
    RIGHT = detectColor(RCOLOR)
    BLOCKCO = sum(BCOLOR.rgb())
    
    flag=False

    ####

    if BLOCKCO > 10 and BLOCKCO < 30:
        turn10right(EV3,L,R)
        return

    if (LEFT=="black") and (RIGHT=="black"):
        return "stop"
        flag=True
    
    if (LEFT=="black") and (RIGHT=="white"):
        return "turn right"
        flag=True
    
    if (LEFT=="black") and (RIGHT=="blue"):
        return "turn left"
        flag=True

    ####
    if (LEFT=="blue") and (RIGHT=="black"):
        return "move on"
        flag=True
    
    if (LEFT=="blue") and (RIGHT=="white"):
        return "move on"
        flag=True
    
    if (LEFT=="blue") and (RIGHT=="blue"):
        return "turn right"
        flag=True
    
    ####
    if (LEFT=="white") and (RIGHT=="black"):
        return "stop"
        flag=True
    
    if (LEFT=="white") and (RIGHT=="white"):
        return "move on"
        flag=True
    
    if (LEFT=="white") and (RIGHT=="blue"):
        return "turn left"
        flag=True

    if flag==False:
        return "turn right"
        EV3.sound.beep()

def turn10right(EV3, L, R, G):
    currG = G.angle()
    while G.angle() != currG-20:
        L.run(-1*_fast())
        R.run(_fast())
    L.stop()
    R.stop()

def forward(EV3,L,R,T,ms):
    start = T.time()
    L.run(_fast())
    R.run(_fast())
    while True:
        if ((T.time())-ms) > start:
            break

def backward(EV3,L,R,T,ms):
    start = T.time()
    L.run(_fastBack())
    R.run(_fastBack())
    while True:
        if ((T.time())-ms) > start:
            break



def driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,message):
    """
    function line-follows robot keeping it central
    until a crossing threshhold met

    T is timer interface
    """
    while True:
        EV3.screen.print(message)
        #print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,message)
        if followLine(EV3,LCOLOR,RCOLOR,BCOLOR,L,R) == "move on":
            L.run(_fast())
            R.run(_fast())
            message = "move on"
        if followLine(EV3,LCOLOR,RCOLOR,BCOLOR,L,R) == "turn right":
            L.run(_fast())
            R.run(_slow())
            message = "turning right"
        if followLine(EV3,LCOLOR,RCOLOR,BCOLOR,L,R) == "turn left":
            L.run(_slow())
            R.run(_fast())
            message = "turning left"
        if followLine(EV3,LCOLOR,RCOLOR,BCOLOR,L,R) == "stop":
            L.stop()
            R.stop()
            message = "stop"
            EV3.screen.print("left "+str(LCOLOR.rgb())+"\n"+"RIGHT "+str(RCOLOR.rgb()) )
            break
        if followLine(EV3,LCOLOR,RCOLOR,BCOLOR,L,R) == "undefined":
            L.stop()
            R.stop()
            #startupSound(EV3)
            message = "undefined"
            
    
    
    

def turn180(EV3, LM, RM, G):
#I implemented this this way because it is easy,
    angleSaved = G.angle()
    while G.angle() <= angleSaved + 180:  # Call G.angle() to get the current angle
        LM.run_time(400, 200, wait=False)
        RM.run_time(-400, 200, wait=False)


def turnTo45(EV3,G,L,R):
    L.run(_fast())
    R.stop()
    #angle=G.angle()
    while G.angle() not in range(42,47):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass


def turnTo90(EV3,G,L,R):
    L.run(_fast())
    R.run(_fastBack())
    #angle=G.angle()
    while G.angle() not in range(87,93):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass

def turnTo0(EV3,G,L,R):
    R.run(_fast())
    L.run(_fastBack())
    #angle=G.angle()
    while G.angle() not in range(-1,2):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass

def pickAndLift(EV3,CLAW,LIFT):
    targetAngle = 1700
    CLAW.run_time(_ContrSpeed(),2000,wait=True) #closing
    LIFT.run_target(400,200,wait=True) #lifting


""" MOTION PROCEDURES"""
"""
#2 
def lineFollowToGamma(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R):
    while(True):
        action = followLine(EV3,LCOLOR,RCOLOR)
        if action == "move on":
            pass
        if action == "turn right":
            pass
"""


"""
def follow_line(ev3,CL,CR):
    rel = (sum(CL.rgb())+1)   /   (sum(CR.rgb())+1)
    if (sum(CL.rgb())<20) and (sum(CR.rgb())<20):
        return "stop"
    if (rel <0.9) and (rel >0.3):
        return "turn left"
    if (rel >1.2 and rel <3.4):
        return "turn right"
    if (rel <= 1.2) and (rel>=0.2):
        return "move on"
    return "undefined"
"""