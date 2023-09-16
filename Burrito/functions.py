from ev3dev2.motor import Motor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor

def startup_sound(EV3):
    """
    sound imitating siren before mechanism started working
    """
    for j in range(3):
        for i in range(100, 1000, 40):
            EV3.speaker.beep(frequency=i, duration=7)

def beep(EV3):
    """
    Little beep - a procedure
    Input: interface to EV3 brick
    """
    EV3.speaker.beep()

def displaySensors(EV3, LCOLOR, BCOLOR, RCOLOR, G):
    """
    prints on 
    """
    pass

def driveToNextThr(EV3, LCOLOR, BCOLOR, RCOLOR, G, L, R):
    """
    function line-follows robot keeping it central
    until a crossing threshold met
    """
    pass

def followLine(EV3, LCOLOR, RCOLOR):
    """return action command to follow the line"""
    rel = (sum(LCOLOR.rgb()) + 1) / (sum(RCOLOR.rgb()) + 1)
    if (sum(LCOLOR.rgb()) < 20) and (sum(RCOLOR.rgb()) < 20):
        return "stop"
    if (rel < 0.9) and (rel > 0.3):
        return "turn left"
    if (rel > 1.2 and rel < 3.4):
        return "turn right"
    if (rel <= 1.2) and (rel >= 0.2):
        return "move on"
    return "undefined"

def turn180(EV3, LCOLOR, BCOLOR, RCOLOR, L, R):
    pass

def turn90Left(EV3, G, L, R):
    currAngle = G.angle()
    while G.angle() < currAngle + 90:
        L.run_time(30, 1, then=L.STOP, wait=False)
        R.run_time(-30, 1, then=R.STOP, wait=False)

def pickAndLift(EV3, CLAW, LIFT):
    pass

""" MOTION PROCEDURES"""
# 2
def lineFollowToGamma(EV3, LCOLOR, BCOLOR, RCOLOR, G, L, R):
    while True:
        action = followLine(EV3, LCOLOR, RCOLOR)
        if action == "move on":
            pass
        if action == "turn right":
            pass
