from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

from pybricksmenu import main_menu, startup_checks

hub = PrimeHub()
hub.light.on(Color.MAGENTA)

motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)

motor_right = Motor(Port.F)

#Robot drove 998 mm out of the 1000 it was supposed to.
wheel_diameter = 88 * 998 / 1000
axel_track = 112

drive = DriveBase(motor_left, motor_right, wheel_diameter,axel_track)

startup_checks(hub)

def mission1():
    drive.straight(1000)

def mission2():
    drive.turn(360)

def mission3():
    drive.straight(600)
    drive.turn(-45)
    drive.straight(300)
    drive.straight(70)
    drive.turn(-70)
    drive.straight(70)
    drive.turn(-110)
    drive.straight(790)

mission = 1

while True:
    # Show the menu and wait for a choice.
    mission = main_menu(hub, num_items = 3, item = mission)

    # Run the chosen mission and the loop back to the menu.
    if mission == 1:
        mission1()
    elif mission == 2:
        mission2()
    elif mission == 3:
        mission3()
