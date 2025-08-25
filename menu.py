"""
Main menu for pybricks, by Joey Parrish, 2025

The pybricks firmware doesn't come with a menu or support for multiple programs
like the default Spike firmware.  This is a simple menu system and basic
startup checks to make it easier for kids to get started coding missions.

The startup checks ensure they don't start missions while plugged in, and show
battery status while charging.  If the battery level is too low on startup, a
warning animation will be shown.  Please charge to avoid inaccuracies caused by
low torque.

Sample usage:


from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

from menu import main_menu, startup_checks


hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
wheel_diameter = 175
wheel_separation = 200
drive = DriveBase(left_motor, right_motor, wheel_diameter, wheel_separation)
mission = 1


def mission1(drive: DriveBase) -> None:
    drive.straight(1000)


def mission2(drive: DriveBase) -> None:
    drive.turn(720)


startup_checks(hub)

while True:
    mission = main_menu(hub, 9, mission)
    if mission == 1:
        mission1(drive)
    elif mission == 2:
        mission2(drive)
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait


def wait_for_button(hub: PrimeHub) -> Set[Button]:
    """Wait for a button to be pressed, then return the buttons.

    Returns a `Set` of `Button` values when the buttons are released.

    Whichever buttons are released last are the ones returned.

    To see if a particular button was pressed, use something like:

    ```py
        from pybricks.parameters import Button
        from menu import wait_for_button

        pressed = wait_for_button(hub)
        if Button.LEFT in pressed:
            print('Left button pressed!')
    ```
    """

    # Wait for any buttons to be pressed, and record them.
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        wait(10)

    # Wait for all buttons to be released.
    while any(hub.buttons.pressed()):
        wait(10)

    # Return the set of pressed buttons.
    return pressed


def main_menu(hub: PrimeHub, num_items: int, item: int = 1) -> int:
    """Display a numerical menu.

    Press left to go down, right to go up, and the center button to choose an
    item.  Returns the number (from 1 to `num_items`) of the chosen item.

    To quit to the bootloader, press the center and bluetooth buttons at the
    same time.

    Sample usage:

    ```py
        # The default mission to show in the menu.
        mission = 1

        while True:
            # Show the menu and wait for a choice.
            mission = main_menu(hub, num_items = 9, item = mission)

            # Run the chosen mission and the loop back to the menu.
            if mission == 1:
                mission1(drive)
            elif mission == 2:
                mission2(drive)
    ```
    """

    # The user can always hold the center button to shut down.  While in the
    # menu, the user can also press bluetooth & center together to quit.
    hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

    while True:
        # Show the number of the selected item.
        hub.display.number(item)

        # Wait for buttons to be pressed.
        pressed = wait_for_button(hub)

        if Button.LEFT in pressed:
            # Go down, and wrap around if needed.
            item -= 1
            if item < 1:
                item = num_items
        elif Button.RIGHT in pressed:
            # Go up, and wrap around if needed.
            item += 1
            if item > num_items:
                item = 1
        elif Button.CENTER in pressed:
            # The user picked something.
            break

    # Allow the center button to act as an emergency stop again.
    hub.system.set_stop_button(Button.CENTER)

    # Return the item the user picked.
    return item


def startup_checks(hub):
    """Run startup checks to make sure it's safe to run.

    Checks charger status and waits until the robot is unplugged.

    Before returning, it checks the robot's battery level.  If it's too low for
    accuracy (too low for consistent torque), it shows a warning animation
    (spinning sad face) on the display for 3 seconds.

    Call this before your menu loop.  (`while True: main_menu(...)`)
    """

    print('charger status', hub.charger.status())
    print('voltage', hub.battery.voltage())
    print('current', hub.battery.current())

    # Check charging status.  We don't want to show the menu and allow programs
    # to run while plugged in.
    status = hub.charger.status()
    while status != 0:
        if status == 1:  # Charging
            icon = Icon.PAUSE
        elif status == 2:  # Charged
            icon = Icon.TRUE
        elif status == 3:  # Error
            icon = Icon.SAD

        # So long as we're plugged in, keep showing the icon.
        hub.display.icon(icon)
        wait(10)
        status = hub.charger.status()

    # If the voltage is low, show a warning animation, but return and let the
    # user decide if they want to use it.
    if hub.battery.voltage() < 8000:
        print('Low voltage!  Please charge me!')
        for side in [Side.TOP, Side.RIGHT, Side.BOTTOM, Side.LEFT, Side.TOP]:
            hub.display.orientation(side)
            hub.display.icon(Icon.SAD)
            wait(500)
        wait(500)


if __name__ == '__main__':
    # A simple test program for the menu.
    hub = PrimeHub()

    print('Running menu demo...')
    hub.display.icon(Icon.CIRCLE)
    wait(3000)

    startup_checks(hub)

    chosen = 1
    while True:
        chosen = main_menu(hub, 9, chosen)
        hub.display.icon(Icon.HEART)
        wait(3000)
