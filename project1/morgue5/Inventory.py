from project1.morgue5.Shared import *


def inventory():
    win_inventory = Window(app, title="Inventory",
                           height=300, width=300,
                           layout="grid")
    win_inventory.show(wait=True)

    Text(win_inventory, text=10 * " ", grid=[0, 0])
    Text(win_inventory, text="Bodies in morgue: " +
                             str(len(bodies)),
         align="right", grid=[1, 1])

    report = ""
    for each in bodies:
        report += str(each) + "\n"

    Text(win_inventory, text=report, grid=[1, 3])

    PushButton(win_inventory, text=" E x i t ", grid=[1, 5],
               command=win_inventory.destroy)
