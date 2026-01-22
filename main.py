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

startup_checks(hub)

# these are only the default not always the argument if new argument is set.
def settings(straight_speed=800, straight_acceleration=(200, 700),
             turn_rate=150, turn_acceleration=(150, 300)):
    drive.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)

def elevator(units: int):
    tool_right.run_angle(speed=500, rotation_angle=units*(-30))

def go_fast():
    settings(straight_acceleration=800)

def arm(forward: bool):
    #-150 brings arm forward fully, +150 brings arm fully back
    if forward:
        angle=-150
    else:
        angle=150
    tool_left.run_angle(speed=500, rotation_angle=angle)

def curved_arm(degrees_turn: float):
    tool_left.run_angle(speed=500, rotation_angle=degrees_turn)

#right side of robot is one thick black line and three
#squares away from the curved line in the red zone facing mission one
#missions 3 (minecart) & 13 (statue)
def run_minecart():
    settings(straight_acceleration=350)
    #gets to the minecart lift (AKA mission 3)
    drive.straight(540)
    #now in top left corner of board
    
    drive.arc(180, 90)
    drive.straight(235)

    #turning to face minecart
    drive.turn(-90)
    drive.straight(18)
    
    #raising minecart
    elevator(20)
    #lowering the handle so we dont knock the cave entrance down, then backing up to release handle
    elevator(-21)

    # turning to face seal
    drive.straight(-40)
    drive.turn(45)
    drive.arc(300, 45)
    drive.straight(-360)
    drive.turn(42)
    drive.straight(135)

    elevator(20)
    #statue now raised

    #gets back to red home
    drive.straight(-330)
    drive.turn(60)
    go_fast()
    drive.straight(800)

#starts after 1 thick black line from corner in blue zone
#mission 7 (millstone)
def run_millstone():
    drive.straight(190)
    drive.turn(80)
    drive.straight(115)
    drive.arc(-155, 70)
    #now on east wall
    #open up arm to get past the silo
    curved_arm(-180)
    #robot will need to redirect itself on the wall and with gyro robot won't do that
    drive.use_gyro(False)
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
    go_fast()
    drive.straight(-600)

# mission 5/6/9/10
# starts on after 2 thick black lines + 1 square from the right side
def run_market():
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
    drive.use_gyro(False)
    go_fast()
    drive.straight(300)
    drive.turn(-45)
    drive.straight(-200)

def run_EMERGENCY():
    # emergency run starts with right side of robot on
    # black line away from the curved red line.
    # then=Stop.NONE is telling the robot to not stop between
    # arc and straight.
    drive.arc(320, 94, then=Stop.NONE)
    drive.straight(1250)

def run_sand():
    # right side of robot on side line on 2 squares 
    #robot all the way on supporters
    settings(straight_acceleration=(100, 100))
    elevator(5)
    drive.straight(497)
    elevator(-7)
    go_fast()
    drive.straight(-70)
    elevator(7)
    drive.straight(-400)

def run_brush():
    #robot drives forward to do the Surface Brushing mission
    #postion: 2 thick line 1 squares
    go_fast()
    drive.use_gyro(True)
    drive.straight(650)
    drive.straight(-610)

def run_silo():
    #right side of jig starts at 0th black line
    #slow down start of mission to make it more accurate
    settings(straight_acceleration=(100, 700))
    drive.straight(370)
    for _ in range(3):
        tool_left.run_angle(100, 180)
        tool_left.run_angle(5e6, -180)
    #want to get back to home fast as possible
    go_fast()
    drive.straight(-370)

def run_ship():
    # jig starts 3+2.Remember to pull jig out before starting.
    tool_left.run_angle(100, 180)  # raise hammer
    drive.use_gyro(True)
    drive.straight(830)
    drive.arc(-150,-70)
    drive.turn(-60)
    go_fast()
    drive.straight(1200)

run = 1

while True:
    # Show the menu and wait for a choice.
    drive.use_gyro(False)
    run = main_menu(hub, num_items = 8, item = run)
    hub.imu.reset_heading(angle=0)
    drive.reset()
    settings()
    drive.use_gyro(True)

    # Run the chosen mission and the loop back to the menu.
    if run == 1:
        run_minecart()
    elif run == 2:
        run_sand()
    elif run == 3:
        run_brush()
    elif run == 4:
        run_ship()
    elif run == 5:
        run_silo()
    elif run == 6:
        run_millstone()
    elif run == 7:
        run_market()
    elif run == 8:
        run_EMERGENCY()

    run = run + 1
