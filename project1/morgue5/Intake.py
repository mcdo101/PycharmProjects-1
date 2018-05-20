from project1.morgue5.Shared import *


def intake():
    global btg_gender

    win_intake = Window(app, title="Intake",
                        height=280, width=400, layout="grid")
    win_intake.show(wait=True)

    Text(win_intake, text=10 * " ", grid=[0, 0])

    btg_gender = ButtonGroup(win_intake,
                             options=[
                                 ["Male", "M"],
                                 ["Female", "F"]
                             ], grid=[1, 1])

    Text(win_intake, text="Name", align="left", grid=[1, 5])
    TextBox(win_intake, width=30, align="left", grid=[2, 5])

    Text(win_intake, text="Age", align="left", grid=[1, 7])
    TextBox(win_intake, width=3, align="left", grid=[2, 7])

    Text(win_intake, text="Height", align="left", grid=[1, 9])
    TextBox(win_intake, width=5, align="left", grid=[2, 9])

    Text(win_intake, text="Weight", align="left", grid=[1, 11])
    TextBox(win_intake, width=5, align="left", grid=[2, 11])

    Text(win_intake, grid=[1, 12])

    PushButton(win_intake, text="  A d d  ", align="left",
               grid=[1, 13], command=add)

    PushButton(win_intake, text=" E x i t ", align="right",
               grid=[2, 13], command=win_intake.destroy)


def add():
    yes_no = yesno(title="The Morgue", text="OK to add")
    if yes_no:
        bodies.append(Corpse(btg_gender.value))
        info(title="The Morgue", text="Added")
        update()
    else:
        info(title="The Morgue", text="Not Added")
