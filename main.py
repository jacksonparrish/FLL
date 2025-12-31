from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricksmenu import main_menu, startup_checks

hub = PrimeHub()
hub.light.on(Color.MAGENTA)

motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.F)

tool_left = Motor(Port.A)
tool_right = Motor(Port.C)

sensor_left = ColorSensor(Port.D)

#Robot drove 998 mm out of the 1000 it was supposed to.
wheel_diameter = 88 * 998 / 1000
#Measured 112 calibrated to this
axel_track = 113.55

drive = DriveBase(motor_left, motor_right, wheel_diameter,axel_track)

competition = False

# these are only the default not always the argument if new argument is set.
def settings(straight_speed=800, straight_acceleration=(200, 700),
             turn_rate=150, turn_acceleration=(150, 300)):
    drive.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)


# slow down faster for faster runs
settings()
startup_checks(hub)


def elevator(units: Number):
    tool_right.run_angle(speed=500, rotation_angle=units*(-30))


def arm(forward: bool):
    #-150 brings arm forward fully, +150 brings arm fully back
    if forward:
        angle=-150
    else:
        angle=150
    tool_left.run_angle(speed=500, rotation_angle=angle)


def curved_arm(degrees_turn: Number):
    tool_left.run_angle(speed=500, rotation_angle=degrees_turn)

#right side of robot is one thick black line and three
#squares away from the curved line in the red zone facing mission one
#missions 3 (minecart) & 13 (statue)
def run1():
    #gets to the minecart lift (AKA mission 3)
    if competition:
        drive.straight(585)
    else:
        drive.straight(555)
    #now in top left corner of board

    drive.arc(180, 100)
    if competition:
        drive.straight(240)
    else:
        drive.straight(255)

    #turning to face minecart
    if competition:
        drive.arc(30, -100)
    else:
        drive.arc(30, -120)

    # beeping so moey will notice if it is not working
    hub.speaker.volume(75)
    hub.speaker.beep(frequency=500, duration=350)
    hub.speaker.volume(50)
    if competition:
        drive.straight(20)
    else:
        drive.straight(20)
    #raising minecart
    elevator(20)

    #lowering the handle so we dont knock the cave entrance down, then backing up to release handle
    elevator(-21)
        
    # turning to face seal
    drive.straight(-20)
    drive.turn(90)
    drive.straight(-84)
    if competition:
        drive.turn(33)
        drive.straight(37)
    else:
        drive.turn(35)
        drive.straight(39)

    elevator(20)
    #statue now raised

    #gets back to red home
    drive.straight(-330)
    drive.turn(70)
    drive.straight(870)


#starts after 1 thick black line from corner in blue zone
#mission 7 (millstone)
def run2():
    drive.straight(190)
    drive.turn(80)
    drive.straight(115)
    drive.arc(-155, 70)
    #now on east wall

    #open up arm to get past the silo
    curved_arm(-180)
    #drives toward the north wall
    drive.straight(470)
    #lets us get closer to the north wall
    curved_arm(90)
    #getting all the way to the north wall
    drive.straight(75)

    curved_arm(100)
    #now have millstone in tool

    # going south to pull millstone 
    drive.straight(-210)
    # to get the curved arm out of the border
    curved_arm(-180)
    

# mission 5/6/9/10
# starts on after 2 thick black lines + 1 square from the right side
def run3():
    #gets robot to push the forge in
    drive.straight(700)
    #pushes who lived here switch
    drive.turn(-35)
    drive.turn(35)
    #backs away from who lived here and gets into position for tip the scales lever
    drive.straight(-110)
    drive.turn(-45)
    drive.straight(300)
    drive.turn(-40)
    drive.straight(170)
    drive.turn(-45)
    arm(forward=True)
    arm(forward=False)

    #moves to clear space without impacting other structures to push market lever 
    drive.turn(40)
    drive.straight(240)
    drive.turn(-180)
    drive.straight(270)
    drive.turn(45)

    #pushes market sliding lever and backs away
    drive.straight(225)
    drive.turn(-45)
    drive.straight(-200)

def run4():
    # emergency run starts with right side of robot on
    # black line away from the curved red line.
    # then=Stop.NONE is telling the robot to not stop between
    # arc and straight.
    drive.arc(320, 94, then=Stop.NONE)
    drive.straight(1250)

def run5():
    #left side of jig is on last black line 
    #robot all the way on supporters
    settings(straight_acceleration=(100, 100))
    elevator(5)
    drive.straight(407)
    elevator(-7)
    drive.straight(-70)
    elevator(20)

def run6(): 
    #robot drives forward to do the Surface Brushing mission
    #postion: 2 thick line 1 squares
    settings(straight_acceleration=800)
    drive.straight(650)
    drive.straight(-600)

def run7():
    #postion: 3 and a half squares no thick lines
    #slow down start of mission to make it more accurate
    settings(straight_acceleration=(100, 700))
    drive.straight(370)
    for _ in range(3):
        tool_left.run_angle(100, 180)
        tool_left.run_angle(5e6, -180)
    #want to get back to home fast as possible
    settings(straight_speed=800, straight_acceleration=800)
    drive.straight(-370)

def run8():
    # jig starts 3+2.Remember to pull jig out before starting.
    drive.straight(810)
    drive.arc(-150,-70)
    drive.turn(-75)
    settings(straight_acceleration=800)
    drive.straight(1200)

run = 1

while True:
    # Show the menu and wait for a choice.
    run = main_menu(hub, num_items = 8, item = run)

    hub.imu.reset_heading(angle=0)
    drive.reset()
    settings()

    # Run the chosen mission and the loop back to the menu.
    if run == 1:
        run1()
    elif run == 2:
        run2()
    elif run == 3:
        run3()
    elif run == 4:
        run4()
    elif run == 5:
        run5()
    elif run == 6:
        run6()
    elif run == 7:
        run7()
    elif run == 8:
        run8()

    run = run + 1
