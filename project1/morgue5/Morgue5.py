from project1.morgue5.Shared import *
from project1.morgue5.Intake import intake
from project1.morgue5.Inventory import inventory
from project1.morgue5.Discharge import discharge


def main():

    Text(app, text="")
    PushButton(app, text="    I n t a k e     ",
               command=intake)

    Text(app, text="")
    PushButton(app, text="D i s c h a r g e",
               command=discharge)

    Text(app, text="")
    PushButton(app, text="I n v e n t o r y",
               command=inventory)

    Text(app, text="")
    PushButton(app, text="       E x i t         ",
               command=exit)

    app.display()


main()
