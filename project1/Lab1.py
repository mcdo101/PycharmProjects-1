from guizero import *


def click():
    txtHello.value = "Hello " + tbxName.value + " " + tbxName2.value


def change_font_size(position):
    txtHello.size = position


def show_hide():
    if cbxShowHide.value:
        click()
    else:
        txtHello.clear()


def set_color():
    txtHello.text_color = btgColor.value


def set_font(value):
    txtHello.font=value


my_window = App(title="My First Window")

txtHello = Text(my_window, text="Hello World", text_color="red", size=14)

tbxName = TextBox(my_window, text="first name", width=20,)

tbxName2 = TextBox(my_window, text="last name", width=20,)

PushButton(my_window, text="ENTER NAME", command=click)

PushButton(my_window, text="QUIT", command=quit)

sldFontSize = Slider(my_window, start=6, end=20, command=change_font_size)

sldFontSize.value = 14

cbxShowHide = CheckBox(my_window, text="Show/Hide the Greeting", command=show_hide)

cbxShowHide.toggle()

btgColor = ButtonGroup(my_window, horizontal=True,
                       options=[["Red", "red"],
                                ["Blue", "blue"],
                                ["Green", "green"]],
                       selected="red", command=set_color)

Combo(my_window, options=["Helvitica", "Times", "Courier"], command=set_font)

my_window.display()
