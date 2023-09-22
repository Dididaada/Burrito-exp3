from pybricks.tools import wait
from pybricks.parameters import Port, Stop, Direction, Button, Color

def detectColor(C):
    if sum(C.rgb())>100: 
        #pure is 200
        return "white"
    if sum(C.rgb())<50:
        return "black"
    return "blue"

def _slow():
    return -80

def _slowBack():
    return 100

def _fast():
    return -250

def _ContrSpeed():
    return -800

def _fastBack():
    return 250

def turnTo0(EV3,G,L,R):
    R.run(_fast())
    L.run(80)
    #angle=G.angle()
    while G.angle() not in range(-1,2):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass

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
    pass

def print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,message):
    """
    EV3.screen.set_font(small_font)
    EV3.screen.clear() 
    EV3.screen.print("LEFT"+str(LCOLOR.rgb())+"\n"+str(sum(LCOLOR.rgb())))
    EV3.screen.print("RIGHT"+str(RCOLOR.rgb())+"\n"+str(sum(RCOLOR.rgb())))
    #EV3.screen.print("Side Sensor"+str(BCOLOR.rgb())+"\n"+str(sum(BCOLOR.rgb())))
    EV3.screen.print("Left+1  / right+1 =" + str((sum(LCOLOR.rgb())+1)   /  \
         (sum(RCOLOR.rgb())+1)))
    EV3.screen.print("Angle "+str(G.angle())+"º")
    EV3.screen.print("DEBUG MESSAGE "+message, end="")
    """
    pass



def followLine(EV3,LCOLOR,RCOLOR):
    #EV3.screen.print(l+str(LCOLOR.rgb())+"==="+r+str(RCOLOR.rgb()))
    LEFT = detectColor(LCOLOR)
    RIGHT = detectColor(RCOLOR)
  


    ####
    if (LEFT=="black") and (RIGHT=="black"):
        return "stop"

    
    if (LEFT=="black") and (RIGHT=="white"):
        return "turn right"
  
    
    if (LEFT=="black") and (RIGHT=="blue"):
        return "turn left"


    ####
    if (LEFT=="blue") and (RIGHT=="black"):
        return "move on"

    
    if (LEFT=="blue") and (RIGHT=="white"):
        return "turn right"

    
    if (LEFT=="blue") and (RIGHT=="blue"):
        return "turn right"

    
    ####
    if (LEFT=="white") and (RIGHT=="black"):
        beep(EV3)
        return "stop"

    
    if (LEFT=="white") and (RIGHT=="white"): 
        return "move on"

    
    if (LEFT=="white") and (RIGHT=="blue"):
        return "turn left"
    return "turn right"


def forward(EV3,L,R,T,ms):
    #start = T.time()
    #L.run(_slow())
    #R.run(_slow())
    L.run(-80)
    R.run(-80)
    wait(ms)
    L.stop()
    R.stop()
    """
    while True:
        if ((T.time())-ms) > start:
            break
    """

def backward(EV3,L,R,T,ms):
    start = T.time()
    L.run(_fastBack())
    R.run(_fastBack())
    while True:
        if ((T.time())-ms) > start:
            break

def turnTodegree(EV3,G,L,R, degrees): 
    L.run(_fast())
    R.stop()
    #angle=G.angle()

    while G.angle() not in range(degrees-2,degrees+2):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass

def tothethresholdsinglecase(EV3,LCOLOR,FCOLOR,RCOLOR,G,L,R,T): 
    while sum(FCOLOR.rgb()) < 1:
        #EV3.screen.print(message)
        #print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,message)
        if followLine(EV3,LCOLOR,RCOLOR) == "move on":
            L.run(_fast())
            R.run(_fast())
            message = "move on"
        if followLine(EV3,LCOLOR,RCOLOR) == "turn right":
            L.run(_fast())
            R.run(_slow())
            message = "turning right"
        if followLine(EV3,LCOLOR,RCOLOR) == "turn left":
            L.run(_slow())
            R.run(_fast())
            message = "turning left"
        

def driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,message):
    """
    function line-follows robot keeping it central
    until a crossing threshhold met

    T is timer interface
    """
    while True:
        #EV3.screen.print(message)
        #print_all_sensors(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R,T,small_font,message)
        if followLine(EV3,LCOLOR,RCOLOR) == "move on":
            L.run(_fast())
            R.run(_fast())
            message = "move on"
        if followLine(EV3,LCOLOR,RCOLOR) == "turn right":
            L.run(_fast())
            R.run(_slow())
            message = "turning right"
        if followLine(EV3,LCOLOR,RCOLOR) == "turn left":
            L.run(_slow())
            R.run(_fast())
            message = "turning left"
        if followLine(EV3,LCOLOR,RCOLOR) == "stop":
            L.stop()
            R.stop()
            message = "stop"
            beep(EV3)
            L.stop()
            R.stop()
            wait(1000)
            break
            
    
    
    

def turn180(EV3, L, R, G, timeout_ms=5000):
    temporary = G.angle()
    L.run(_fast())
    R.stop(_fastBack())
    
    while G.angle() < temrorary + 180: 
        pass 

    # Stop the motors
    L.stop()
    R.stop()



def turnTo45(EV3,G,L,R):
    L.run(_fast())
    R.stop()
    #angle=G.angle()
    while G.angle() not in range(53,57):
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

def turnTo90left(EV3,G,L,R):
    L.run(_fastBack())
    R.run(_fast())
    #angle=G.angle()
    while G.angle() not in range(87,93):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass

def turnTo15(EV3,G,L,R):
    L.run(_fast())
    R.run(_fastBack())
    #angle=G.angle()
    while G.angle() not in range(14,17):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass
def pickupFromSense(EV3, G, L, R, CLAW, LIFT,T):  
    LIFT.run(500)
    wait(500)
    LIFT.stop()
    turnTo15left(EV3,G,L,R)
    LIFT.run(-500)
    wait(500)
    LIFT.stop()
    pickAndLift(EV3,CLAW,LIFT)
def turnTo15left(EV3,G,L,R):
    L.run(_fastBack())
    R.run(_fast())
    #angle=G.angle()
    while G.angle() not in range(-17,-14):
        EV3.screen.print(G.angle())
        pass
    L.stop()
    R.stop()
    pass

def rotateToInitialAngle(EV3, G, L, R, initial_angle):
    target_angle = initial_angle
    while G.angle() != target_angle:
        if G.angle() < target_angle:
            L.run(_fast())
            R.run(_fastBack())
        else:
            L.run(_fastBack())
            R.run(_fast())
    
    L.stop()
    R.stop()

# Fucjing grabbing mechanisms picks up the box 
def pickAndLiftOp(EV3,CLAW,LIFT):
    targetAngle = 1700
    CLAW.run_target(_ContrSpeed(),-targetAngle,wait=True) #closing
    #CLAW.run_target(targetSpeed,targetAngle,wait=True) #opening

    LIFT.run_target(_ContrSpeed(),targetAngle,wait=True) #lifting

#
def pickAndLiftCl(EV3, CLAW, LIFT):
    targetAngle = 1700
    CLAW.run_target(_ContrSpeed(),targetAngle,wait=True) #opening
    CLAW.run_target(_ContrSpeed(),-targetAngle,wait=True) #closing
    LIFT.run_target(_ContrSpeed(),targetAngle,wait=True) #lifting
def pickAndLift(EV3,CLAW,LIFT):
    targetAngle = 1700
    CLAW.run_time(_ContrSpeed(),2000,wait=True) #closing
    LIFT.run_target(400,200,wait=True) #lifting
def putAndLowerClaw(EV3, CLAW, LIFT):
    targetClawAngle = -1200  # Adjust the target angle for opening the claw
    targetLiftAngle = -1200  # Adjust the target angle for lowering the lift

    LIFT.run_target(_ContrSpeed(), targetLiftAngle, wait=True)
    # Open the claw
    CLAW.run_target(-1*_ContrSpeed(), targetClawAngle, wait=True)

    # Lower the lift
def liftAndOpen(EV3, CLAW, LIFT):
    #targetAngle = 1700
    EV3.speaker.beep(frequency=500, duration=100)
    EV3.speaker.beep(frequency=1500, duration=100)
    EV3.speaker.beep(frequency=1500, duration=100)
    EV3.screen.print("CLAW angle "+str(CLAW.angle()))
    EV3.screen.print("LIFT angle "+str(LIFT.angle()))

    LIFT.run_target(200, 160, then=Stop.HOLD, wait=True) # move the fork up to 50 degrees

    CLAW.run_target(200, 1000, wait=True)
    CLAW.run_target(200, 0, wait=True)
    LIFT.run_target(200, 80, then=Stop.HOLD, wait=True) # move the fork up to 80 degrees to get it up from ship

    """
    CLAW.run_target(200, 1200, wait=True)  # Opening the claw
    LIFT.run_target(200, 1500, wait=True)  # Lifting
    """ 

def liftForkUp(EV3, LIFT):
    EV3.screen.clear()
    EV3.screen.print("LIFT angle "+str(LIFT.angle()))
    LIFT.run_target(200, 160, then=Stop.HOLD, wait=True) # Move the fork up to 160 degrees and hold

def prepareToTakeObject(EV3, LIFT):
    LIFT.run_target(200, 57, wait=True) # Put the LIFT to 53 degrees

def openAndCloseFork(EV3, CLAW):
    CLAW.run_target(200, 1000, wait=True) # Open the claw
    CLAW.run_target(200, 0, wait=True)    # Close the claw

def open(EV3, CLAW): 
    CLAW.run_target(400, 1000, wait=True)
    
def close(EV3, CLAW): 
    CLAW.run_target(200, 0, wait=True)

def putObjectTo80Degrees(EV3, LIFT):
    LIFT.run_target(200, 90, then=Stop.HOLD, wait=True) # Put the object to 80 degrees

    
def resetClawToInitial(EV3, CLAW):
    targetClawAngle = 0  # Adjust the target angle for the initial position

    # Move the claw to the initial position
    CLAW.run_target(_ContrSpeed(), targetClawAngle, wait=True)

def deetectFront(EV3,FCOLOR):
    if sum(FCOLOR.rgb())>=2:
        return "some col other than black"
    return "different"

def beep_if_gyro_not_zero(EV3, G):
    while True:
        current_angle = G.angle()

        if current_angle != 0:
            for _ in range(4):
                EV3.speaker.beep()
            return