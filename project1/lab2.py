from guizero import *
from math import pi


def calc():
    try:
        diameter = float(tbxDiameter.value)
        if diameter > 1000:
            warn(title="Circle Caluclator", text="That's a really big circle")
        if diameter >= 0:
            radius = diameter / 2
            area = pi * radius ** 2
            circumfrence = pi * diameter
            txtArea.value = round(area, 1)
            txtCircumfrence.value = round(circumfrence, 1)

        else:
            txtCircumfrence.clear()
            txtArea.clear()
            error(title="Circle Calculator", text="Negative value not valid")
    except ValueError:
        error(title="Circle Caluclator", text="Bad or missing value")


window = App(title="Second Project", width=350, height=250, layout="grid")

Text(window, text=" " * 5,size=20, grid=[0, 0])

Text(window, text="Diameter ", grid=[1, 1])
tbxDiameter= TextBox(window, grid=[2, 1])

Text(window, grid=[0, 2])

PushButton(window, text="CALC", grid= [1, 3], command=calc)
PushButton(window, text="QUIT", grid=[2, 3], command=quit)

Text(window, grid= [0, 4])

Text(window, text="Area ", align="right", grid=[1, 5])
txtArea = Text(window, grid=[2, 5])

Text(window, text="Circumfrence ", align="right", grid=[1, 7])
txtCircumfrence = Text(window, grid=[2, 7])

window.display()
