from random import randint
from guizero import *

app = None

pb_start = pb_stop = pb_clear = None
txt_head_count = txt_head_pct = txt_tail_count = txt_tail_pct = None
picture = None


def next_cycle():
    picture.value = "penny blank.gif"
    picture.after(1000, next_flip)


def next_flip():
    number_of_heads = int(txt_head_count.value)
    number_of_tails = int(txt_tail_count.value)

    toss = randint(0, 1)
    if toss == 0:
        picture.value = "penny head.gif"
        number_of_heads += 1
        txt_head_count.value = str(number_of_heads)
    else:
        picture.value = "penny tail.gif"
        number_of_tails += 1
        txt_tail_count.value = str(number_of_tails)

    total_flips = number_of_heads + number_of_tails
    if total_flips > 0:
        txt_head_pct.value = str(round(number_of_heads*100/total_flips))
        txt_tail_pct.value = str(round(number_of_tails*100/total_flips))


def clear():
    txt_head_count.value = "0"
    txt_head_pct.value = "0"
    txt_tail_count.value = "0"
    txt_tail_pct.value = "0"
    pb_clear.disable()
    picture.value = "penny blank.gif"


def stop():
    app.cancel(next_cycle)
    pb_stop.disable()
    pb_start.enable()
    pb_clear.enable()


def start():
    app.repeat(2000, next_cycle)
    pb_stop.enable()
    pb_start.disable()
    pb_clear.disable()


def main():
    global pb_start, pb_stop, pb_clear, app
    global txt_head_count, txt_head_pct, txt_tail_count, txt_tail_pct
    global picture

    app = App(title="Second Project", width=566, height=488, layout="grid")

    picture = Picture(app, image="penny blank.gif", grid=[1, 0])

    Text(app, text=" " * 30, size=10, grid=[0, 0])

    pb_start = PushButton(app, text="START", grid=[0, 3], command=start)
    pb_stop = PushButton(app, text=" STOP ", grid=[0, 4], command=stop)
    pb_clear = PushButton(app, text="CLEAR", grid=[0, 5], command=clear)
    PushButton(app, text=" QUIT ", grid=[0, 6], command=quit)

    pb_clear.disable()
    pb_stop.disable()

    Text(app, text="# of heads: ", grid=[1, 3], align="right")
    txt_head_count = Text(app, text="0", align="left", grid=[2, 3])

    Text(app, text="% of heads: ", grid=[1, 4], align="right")
    txt_head_pct = Text(app, text="0", align="left", grid=[2, 4])

    Text(app, text="# of tails: ", grid=[1, 5], align="right")
    txt_tail_count = Text(app, text="0", align="left", grid=[2, 5])

    Text(app, text="% of tails: ", grid=[1, 6], align="right")
    txt_tail_pct = Text(app, text="0", align="left", grid=[2, 6])

    app.display()


main()
