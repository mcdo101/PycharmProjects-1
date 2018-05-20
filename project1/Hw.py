from guizero import *

my_window = App(title="My First Window")

my_window_2 = App(title="My Second Window")

tbxName = TextBox(my_window_2, text="first name", width=20,)

tbxName2 = TextBox(my_window_2, text="last name", width=20,)

my_window_2.display()