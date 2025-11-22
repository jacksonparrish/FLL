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
    tool_left.run_angle(speed=500, rotation_angle=-150)


def curved_arm(degrees_turn: Number):
    tool_left.run_angle(speed=500, rotation_angle=degrees_turn)

#right side of robot is one thick black line and three
#squares away from the curved line in the red zone facing mission one
#moves to minecart then statue
def run1():
    #gets to the minecart lift (AKA mission 3)
    drive.straight(590)
    #now in top left corner of board

    drive.arc(130, 90)
    drive.straight(270)
    
    #turning to face mincart
    drive.turn(-80)

    #raising minecart
    elevator(20)
    
    #lowering the handle so we dont knock the cave entrance down, then backing up to release handle
    elevator(-20)
    drive.straight(-15)
    

    drive.turn(90)
    drive.straight(-20)

    drive.turn(45)
    drive.straight(35)

    drive.turn(-20)
    elevator(25)

    #statue now raised

    #gets to blue home from mission 13
    drive.straight(-50)
    drive.arc(300, -35)

    drive.straight(1000)
    drive.arc(250, 90)
    drive.straight(500)

def run2():
    # starts after 1 thick black line from corner in blue zone
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
    


# mission 5/6/9
# starts on after 2 thick black lines + 1 square from the right side
def run3():
    #gets robot to push the forge in
    drive.straight(700)
    #pushes who lived here switch
    drive.turn(-35)
    #backs away from who lived here
    drive.straight(-70)
    #gets into position for tip the scales
    drive.arc(-300, 80)
    arm()

    # moves into open space 
    drive.straight(-110)
    #gets front of robot facing marketplace lever
    drive.turn(25)
    drive.straight(325)
    drive.turn(-150)
    drive.straight(600)


def run4():
    drive.straight(-65)


def run5():
    elevator(10)

def run6():
    drive.arc(305,-30)


run = 1

while True:
    # Show the menu and wait for a choice.
    run = main_menu(hub, num_items = 6, item = run)

    hub.imu.reset_heading(angle=0)
    drive.reset()

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
    
    run = run + 1
