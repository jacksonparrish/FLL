from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricksmenu import main_menu, startup_checks

hub = PrimeHub()
hub.light.on(Color.MAGENTA)

motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.F)

tool_left = Motor(Port.A)
tool_right = Motor(Port.C)

#Robot drove 998 mm out of the 1000 it was supposed to.
wheel_diameter = 88 * 998 / 1000
#Measured 112 calibrated to this
axel_track = 113.55

drive = DriveBase(motor_left, motor_right, wheel_diameter,axel_track)
# these are only the default not always the argument if new argument is set.
def settings(straight_speed=800, straight_acceleration=(300, 700),
             turn_rate=150, turn_acceleration=(150, 300)):
    drive.settings(straight_speed, straight_acceleration,turn_rate, turn_acceleration)


# slow down faster for faster runs
settings()
startup_checks(hub)

def run1():
    drive.straight(1000)

def run2():
    drive.turn(360)

# mission 9
# starts on 2 thick black lines and 2 squares from the right (sign facing)
def run3():
    drive.straight(600)
    drive.turn(-45)
    drive.straight(370)
    drive.turn(-70)
    drive.straight(70)
    drive.turn(-110)
    drive.straight(200)

# mission 5/6/9
# starts on after 2 thick black lines + 3 squares
def run4():
    drive.straight(700)
    #in between the forge and the flip thingie. just finished forge.
    drive.turn(-35)
    #flip thingie done
    drive.straight(-50)
    drive.turn(-30)
    #back up and reposition
    drive.straight(185)
    drive.turn(-25)
    #geting closer to the correct position.
    drive.straight(180) 
    drive.turn(25)
    #repsitioning the robot to have the rear facing market lever
    settings(straight_acceleration=(2000,2000), straight_speed=300)
    drive.straight(-240)
    return
    settings()
    drive.straight(100)



def run5():
    tool_left.run(180)
    tool_right.run(180)

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
