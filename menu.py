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


if __name__ == '__main__':
    # A simple test program for the menu.
    print('Running menu demo...')
    hub = PrimeHub()
    hub.display.icon(Icon.CIRCLE)
    wait(3000)
    chosen = 1
    while True:
        chosen = main_menu(hub, 9, chosen)
        hub.display.icon(Icon.HEART)
        wait(3000)

