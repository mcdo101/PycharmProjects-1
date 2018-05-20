from project1.morgue5.Shared import *


def discharge():
    global tbx_delete_id, win_discharge

    win_discharge = Window(app, title="Discharge",
                           height=300, width=300,
                           layout="grid")
    win_discharge.show(wait=True)

    Text(win_discharge, text=10 * " ", grid=[0, 0])
    Text(win_discharge, text="ID : Gender : Name",
         align="right", grid=[1, 1])

    report = ""
    for each in bodies:
        report += str(each) + "\n"

    Text(win_discharge, text=report, grid=[1, 3])

    Text(win_discharge, text="Enter ID to Delete ",
         align="right", grid=[1, 5])
    tbx_delete_id = TextBox(win_discharge,
                            align="left", grid=[2, 5])

    Text(win_discharge, grid=[1, 6])

    PushButton(win_discharge, text=" D e l e t e ",
               grid=[1, 7], command=remove)
    PushButton(win_discharge, text=" E x i t ", grid=[2, 7],
               command=win_discharge.destroy)


def remove():
    try:
        delete_id = int(tbx_delete_id.value)
        index_id = None
        found = False
        gone = None
        for each in bodies:
            if delete_id == each.index:
                index_id = bodies.index(each)
                gone = each
                found = True
                break

        if found:
            yes_no = yesno(title="The Morgue",
                           text="Confirm discharging id " + str(gone))
            if yes_no:
                del bodies[index_id]
                win_discharge.destroy()
                update()

        else:
            error(title="The Morgue", text="ID not found")
    except ValueError:
        error(title="The Morgue", text="ID must be an integer")
