from pybricks.hubs import PrimeHub

from pybricksmenu import main_menu, startup_checks

hub = PrimeHub()

startup_checks(hub)

def mission1():
    print("ImADoOfUS")

def mission2():
    print("IMadUMmy")

def mission3():
    print("mEdORkY")

mission = 1

while True:
    # Show the menu and wait for a choice.
    mission = main_menu(hub, num_items = 9, item = mission)

    # Run the chosen mission and the loop back to the menu.
    if mission == 1:
        mission1()
    elif mission == 2:
        mission2()
    elif mission == 3:
        mission3()
