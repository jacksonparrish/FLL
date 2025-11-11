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
# these are only the default not always the argument if new argument is set.
def settings(straight_speed=800, straight_acceleration=(200, 700),
             turn_rate=150, turn_acceleration=(150, 300)):
    drive.settings(straight_speed, straight_acceleration,turn_rate, turn_acceleration)


# slow down faster for faster runs
settings()
startup_checks(hub)


def elevator(units: Number):
    tool_right.run_angle(speed=500, rotation_angle=units*(-30))


def arm():
    #never change rotation_angle because we are only using arm once during run 3
    #115 for rotation_angle means that we move the arm all the way forward 
    tool_left.run_angle(speed=500, rotation_angle=-115)

#right side of robot is one thick black line and three
#squares away from the curved line in the red zone facing mission one
#moves to minecart then statue
def run1():
    #gets to the minecart lift (AKA mission 3)
    drive.straight(595)
    #now in top left corner of board

    drive.arc(130, 90)
    drive.straight(280)
    
    #turning to face mincart
    drive.turn(-90)

    #raising minecart
    elevator(20)

    #lowering the handle so we dont knock the cave entrance down, then backing up to release handle
    elevator(-20)
    drive.straight(-20)

    drive.turn(60)
    drive.straight(370)
    #now in the middle-top of the board
    drive.turn(110)
    #now facing middle-bottom of the board
    drive.straight(645)
    #next to the seal
    drive.turn(140)
    drive.straight(230)
    return
    


    #gets to blue home from mission 13
    

def run2():
    # starts after 1 thick black line from corner in blue zone
    drive.straight(300)
    drive.turn(90)
    drive.straight(100)
    drive.arc(-155, 90)
    #now on wall
    drive.straight(430)
    #now in top-right corner
    #getting millstone
    return
    tool_left()
    


# mission 5/6/9
# starts on after 2 thick black lines + 3 squares from the right side
def run3():
    #gets robot to push the forge in
    drive.straight(700)
    #pushes who lived here switch
    drive.turn(-35)

    #gets robot in position for tip the scales lever
    drive.straight(-50)
    drive.turn(-30)
    drive.straight(168)
    drive.arc(-210, 55)
    drive.straight(-30)
    arm()
    drive.straight(-25)
    drive.arc(35,-90)

def run4():
    settings(straight_acceleration=1000, turn_acceleration=1000)
    while sensor_left.color() != Color.BLUE:
        drive.arc(-50,150)
    settings()


def run5():
    elevator(10)

def run6():
    tool_left.run_angle(180, 360)
    tool_right.run_angle(180, 360)
    drive.straight(-40)
run = 1

while True:
    # Show the menu and wait for a choice.
    run = main_menu(hub, num_items = 6, item = run)

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
