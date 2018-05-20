from guizero import *


def calc():
    try:
        length = float(tbxLength.value)
        width = float(tbxWidth.value)
        area = length * width
        perimeter = length * 2 + width * 2
        txtArea.value = round(area, 1)
        txtPerimeter.value = round(perimeter, 1)
    except ValueError:
        error(title="P/A", text="Bad or missing value")


window = App(title="Second Project", width=350, height=250, layout="grid")

Text(window, text=" " * 5,size=20, grid=[0, 0])

Text(window, text="Length ", grid=[1, 1])
tbxLength= TextBox(window, grid=[2, 1])

Text(window, text="Width ", grid=[1, 3])
tbxWidth= TextBox(window, grid=[2, 3])

Text(window, grid=[0, 4])

PushButton(window, text="CALC", grid= [1, 5], command=calc)
PushButton(window, text="QUIT", grid=[2, 5,], command=quit)

Text(window, grid= [0, 6])

Text(window, text="Area: ", align="right", grid=[1, 7])
txtArea = Text(window, grid=[2, 7])

Text(window, text="Perimeter: ", align="right", grid=[1, 9])
txtPerimeter = Text(window, grid=[2, 9])

window.display()
