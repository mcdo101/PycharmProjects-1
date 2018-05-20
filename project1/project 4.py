from guizero import *

pb_start = pb_stop = pb_clear = None


def main():
    app = App(title="Second Project", width=566, height=488, layout="grid")

    pb_start = PushButton(app, text="", grid=[0, 3], command=None)
    pb_stop = PushButton(app, text=" STOP ", grid=[0, 4], command=None)
    pb_clear = PushButton(app, text="CLEAR", grid=[0, 5], command=None)
    PushButton(app, text=" QUIT ", grid=[0, 6], command=quit)

    app.display()


main()