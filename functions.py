def beep(EV3):
    """
    Little beep  - a procedure
    Input: interface to EV3 brick
    """
    EV3.speaker.beep()

def displaySensors(EV3,LCOLOR,BCOLOR,RCOLOR,G):
    """
    prints on
    """
    pass
    

def driveToNextThr(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R):
    """
    function line-follows robot keeping it central
    until a crossing threshhold met
    """
    pass

def followLine(EV3,LCOLOR,RCOLOR):
    """return action command to follow line """

    rel = (sum(LCOLOR.rgb())+1)   /   (sum(RCOLOR.rgb())+1)
    if (sum(LCOLOR.rgb())<20) and (sum(RCOLOR.rgb())<20):
        return "stop"
    if (rel <0.9) and (rel >0.3):
        return "turn left"
    if (rel >1.2 and rel <3.4):
        return "turn right"
    if (rel <= 1.2) and (rel>=0.2):
        return "move on"
    return "undefined"

def turn180(EV3, LM, RM, G):
#I implemented this this way because it is easy,
    angleSaved = G.angle()
    while G.angle() <= angleSaved + 180:  # Call G.angle() to get the current angle
        LM.run_time(400, 200, wait=False)
        RM.run_time(-400, 200, wait=False)

def turn90(EV3, LM, RM, G):
    angleSaved = G.angle()
    while G.angle() <= angleSaved + 90:  # Call G.angle() to get the current angle
        LM.run_time(400, 100, wait=False)
        RM.run_time(-400, 100, wait=False)

def pickAndLift(EV3,CLAW,LIFT):
    pass


""" MOTION PROCEDURES"""
#2 
def lineFollowToGamma(EV3,LCOLOR,BCOLOR,RCOLOR,G,L,R):
    
    while(True):
        action = followLine(EV3,LCOLOR,RCOLOR)
        if action == "move on":
            pass
        if action == "turn right":
            pass
    pass
