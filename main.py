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
# slow down faster for faster runs
drive.settings(straight_speed=800, straight_acceleration=(300, 700),
               turn_rate=150, turn_acceleration=(150, 300))

startup_checks(hub)

def mission1():
    drive.straight(1000)

def mission2():
    drive.turn(360)

# mission 9
# starts on 2 thick black lines and 2 squares from the right (sign facing)
def mission3():
    drive.straight(600)
    drive.turn(-45)
    drive.straight(370)
    drive.turn(-70)
    drive.straight(70)
    drive.turn(-110)
    drive.straight(200)

# mission 5/6
# starts on after 2 thick black line and two squares
def mission4():
    drive.straight(700)
    drive.turn(-35)
    drive.turn(45)

def mission5():
    tool_left.run(180)
    tool_right.run(180)


mission = 1

while True:
    # Show the menu and wait for a choice.
    mission = main_menu(hub, num_items = 5, item = mission)

    # Run the chosen mission and the loop back to the menu.
    if mission == 1:
        mission1()
    elif mission == 2:
        mission2()
    elif mission == 3:
        mission3()
    elif mission == 4:
        mission4()
    elif mission == 5:
        mission5()