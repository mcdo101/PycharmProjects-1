from guizero import *

tbx_finish_times = []
txt_winning_time = None


def calc():
    finish_times = []

    for each in tbx_finish_times:
        if each.value != "":

            try:
                finish_times.append(float(each.value))
            except ValueError:
                error(title="Horse Race", text="Bad value")
                each.focus()
                return

    if len(finish_times) != 0:
        txt_winning_time.value = min(finish_times)
    else:
        txt_winning_time.clear()


def main():
    global tbx_finish_times, txt_winning_time

    window = App(title="Horse Race", width=350, height=250, layout="grid")
    Text(window, text=" " * 5, size=20, grid=[0, 0])

    Text(window, text="Horse 1 ", grid=[1, 1])
    tbx_horse1 = TextBox(window, grid=[2, 1])

    Text(window, text="Horse 2 ", grid=[1, 2])
    tbx_horse2 = TextBox(window, grid=[2, 2])

    Text(window, text="Horse 3 ", grid=[1, 3])
    tbx_horse3 = TextBox(window, grid=[2, 3])

    Text(window, text="Horse 4 ", grid=[1, 4])
    tbx_horse4 = TextBox(window, grid=[2, 4])

    Text(window, text="Horse 5 ", grid=[1, 5])
    tbx_horse5 = TextBox(window, grid=[2, 5])

    tbx_finish_times = [tbx_horse1, tbx_horse2, tbx_horse3, tbx_horse4, tbx_horse5]

    PushButton(window, text="CALC", grid=[1, 6], command=calc)
    PushButton(window, text="CLEAR", grid=[2, 6], command=clear)
    PushButton(window, text="QUIT", grid=[3, 6], command=quit)

    Text(window, text="Winning Time ", grid=[1, 7])
    txt_winning_time = Text(window, grid=[2, 7])

    window.display()


def clear():
    for each in tbx_finish_times:
        each.clear()

main()
