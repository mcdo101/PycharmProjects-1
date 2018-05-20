from guizero import *

# global lists

tbx_entries = []
txt_finishes = []


def calc():
    finish_times = {}
    finish_list = []
    for each in range(len(tbx_entries)):
        if tbx_entries[each][0].value != "":
            if tbx_entries[each][1].value != "":
                finish_times[tbx_entries[each][0].value] = float(tbx_entries[each][1].value)
    print(finish_times)
    for each in sorted(finish_times, key=finish_times.get):
        finish_list.append([each, finish_times[each]])
    for each in range(len(finish_list)):
        txt_finishes[each][0].value = finish_list[each][0]
        txt_finishes[each][1].value = finish_list[each][1]


def main():
    global tbx_entries, txt_finishes

    window = App(title="Horse Race", width=350, height=250, layout="grid")
    Text(window, text=" " * 5, size=10, grid=[0, 0])

    Text(window, text="Horse Names", grid=[0, 1])

    tbx_horse1 = TextBox(window, grid=[0, 2])

    tbx_horse2 = TextBox(window, grid=[0, 3])

    tbx_horse3 = TextBox(window, grid=[0, 4])

    tbx_horse4 = TextBox(window, grid=[0, 5])

    tbx_horse5 = TextBox(window, grid=[0, 6])

    Text(window, text="Finish Times", grid=[2, 1])

    tbx_finish_time1 = TextBox(window, grid=[2, 2])

    tbx_finish_time2 = TextBox(window, grid=[2, 3])

    tbx_finish_time3 = TextBox(window, grid=[2, 4])

    tbx_finish_time4 = TextBox(window, grid=[2, 5])

    tbx_finish_time5 = TextBox(window, grid=[2, 6])

    tbx_entries = [[tbx_horse1, tbx_finish_time1],
                   [tbx_horse2, tbx_finish_time2],
                   [tbx_horse3, tbx_finish_time3],
                   [tbx_horse4, tbx_finish_time4],
                   [tbx_horse5, tbx_finish_time5]]

    PushButton(window, text="SORT", grid=[0, 7], command=calc)
    PushButton(window, text="CLEAR", grid=[2, 7], command=clear)
    PushButton(window, text="QUIT", grid=[3, 7], command=quit)

    Text(window, text="Sorted ", grid=[3, 1])

    txt_name1 = Text(window, grid=[3, 2])

    txt_name2 = Text(window, grid=[3, 3])

    txt_name3 = Text(window, grid=[3, 4])

    txt_name4 = Text(window, grid=[3, 5])

    txt_name5 = Text(window, grid=[3, 6])

    Text(window, text="List ", grid=[4, 1])

    txt_time1 = Text(window, grid=[4, 2])

    txt_time2 = Text(window, grid=[4, 3])

    txt_time3 = Text(window, grid=[4, 4])

    txt_time4 = Text(window, grid=[4, 5])

    txt_time5 = Text(window, grid=[4, 6])

    txt_finishes = [[txt_name1, txt_time1],
                    [txt_name2, txt_time2],
                    [txt_name3, txt_time3],
                    [txt_name4, txt_time4],
                    [txt_name5, txt_time5]]

    window.display()


def clear():
    for each in txt_finishes:
        each.clear()

main()
