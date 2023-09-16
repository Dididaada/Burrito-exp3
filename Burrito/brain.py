def startup_sound(ev3):
    """
    sound imitating siren before mechanism started working
    """
    for j in range(3):
        for i in range(100,1000,40):
            ev3.speaker.beep(frequency=i, duration=7)


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




def follow_line_until_crossing(ev3,CL,CR,G,LM,RM):
    while (True):
        if (sum(CL.rgb())) < 10 and (sum(CR.rgb()) <10):
            ev3.screen.print("Exited color THR")
            ev3.screen.print(sum(CL.rgb()))
            ev3.screen.print(sum(CR.rgb()))
            break
        if (G.angle()>start_angle+2):
            RM.run(-500)
            LM.run(-400)
            ev3.screen.print("<---")
        if G.angle()<start_angle-2:
            RM.run(-400)
            LM.run(-500)
            ev3.screen.print("--->")




def print_all_sensors(ev3,CL,CR,G):
    ev3.screen.print("LEFT"+str(CL.rgb())+"\n"+str(sum(CL.rgb())))
    ev3.screen.print("RIGHT"+str(CR.rgb())+"\n"+str(sum(CR.rgb())))
    ev3.screen.print("Angle "+str(G.angle())+"º", end="")

def print_rel(ev3,CL,CR):
    ev3.screen.print("Left/right =")
    ev3.screen.print(    (sum(CL.rgb())+1)   /   (sum(CR.rgb())+1)      )



""" pieces of example and junk code """
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.

#RM.run_target(500, 2*360)
#LM.run_target(500, 2*360)

# Play another beep sound.
#ev3.speaker.beep(frequency=1000, duration=500)
"""
while(True):
    brain.print_all_sensors(ev3,CL,CR,G)
    wait(2000)
    ev3.screen.clear()
"""


"""
# old piece - running motors
ev3.screen.print("Time: "+str(start))
while True:
    RM.run(500)
    LM.run(500)
    if t.time()-start>1000:
        break
RM.stop()
LM.stop()
ev3.screen.print("Time: "+str(t.time()))

"""