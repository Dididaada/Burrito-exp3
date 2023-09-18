#imports
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.tools import wait
from pybricks.parameters import Stop

#constants

def _ContrSpeed():
    return 800

def _Black():
    return 15

def _White():
    return 35



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

def pickAndLiftOp(EV3,CLAW,LIFT):
    targetAngle = 1700
    CLAW.run_target(_ContrSpeed(),-targetAngle,wait=True) #closing
    #CLAW.run_target(targetSpeed,targetAngle,wait=True) #opening

    LIFT.run_target(_ContrSpeed(),targetAngle,wait=True) #lifting

def pickAndLiftCl(EV3, CLAW, LIFT):
    targetAngle = 1700
    CLAW.run_target(_ContrSpeed(),targetAngle,wait=True) #opening
    CLAW.run_target(_ContrSpeed(),-targetAngle,wait=True) #closing
    LIFT.run_target(_ContrSpeed(),targetAngle,wait=True) #lifting

#PID version of line follower, works but its kinda slow
def line_following_pid(ev3, left_motor, right_motor, left_color_sensor, right_color_sensor,
                       BLACK_THRESHOLD_L, BLACK_THRESHOLD_R, WHITE_THRESHOLD_L, WHITE_THRESHOLD_R,
                       BLUE_THRESHOLD, KP, KI, KD, MAX_INTEGRAL, MIN_INTEGRAL, SLOW_SPEED, SPEED_INCREMENT):
    # Initialize PID variables.
    prev_error = 0
    integral = 0

    while True:
        # Read color sensor values.
        left_color = sum(left_color_sensor.rgb())
        right_color = sum(right_color_sensor.rgb())

        # Calculate the error based on the position relative to the desired white line.
        error = (right_color - left_color) - (WHITE_THRESHOLD_R - WHITE_THRESHOLD_L)

        # Calculate the PID terms.
        proportional = KP * error
        integral += KI * error
        derivative = KD * (error - prev_error)

        # Anti-windup: Limit the integral term.
        if integral > MAX_INTEGRAL:
            integral = MAX_INTEGRAL
        elif integral < MIN_INTEGRAL:
            integral = MIN_INTEGRAL

        # Calculate the motor speeds based on the PID control with smaller increments.
        left_speed = SLOW_SPEED + proportional + integral + derivative
        right_speed = SLOW_SPEED - proportional - integral - derivative

        # Ensure both motors are running with smaller increments.
        left_motor.dc(left_motor.speed() + (left_speed - left_motor.speed()) * SPEED_INCREMENT)
        right_motor.dc(right_motor.speed() + (right_speed - right_motor.speed()) * SPEED_INCREMENT)

        # Check if either sensor detects blue (off-course).
        if left_color <= BLUE_THRESHOLD or right_color <= BLUE_THRESHOLD:
            # Robot is off-course, stop both motors.
            left_motor.stop(Stop.BRAKE)
            right_motor.stop(Stop.BRAKE)
            integral = 0  # Reset the integral term when off-course.

        # Update previous error for the next iteration.
        prev_error = error

        # Add a delay to control the update rate of the PID controller.
        wait(10) 


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
