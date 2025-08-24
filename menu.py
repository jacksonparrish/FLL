from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait


def wait_for_button(hub: PrimeHub) -> Set[Button]:
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

