# Shared import
from guizero import *
import os

# Global widget
app = App(title="Welcome to the Morgue",
          height=300, width=300)

# Global data file and id counter file
data_file = "bodies.pickled"
id_counter_file = "counter.txt"

# Global list
bodies = []


# Global class
class Corpse:

    def __init__(self, gender):
        global in_file

        # Does the id counter file exist?
        id_counter = None
        if os.path.isfile(id_counter_file):
            # Yes, get the id counter from the file
            with open(id_counter_file, "r") as in_file:
                for line in in_file:
                    id_counter = int(line)
        else:
            id_counter = 0

        # Increment the counter
        # Note, it is never decremented
        id_counter = id_counter + 1

        # Write the id_counter to the file
        with open(id_counter_file, "w") as out_file:
            out_file.write(str(id_counter))

        self.index = id_counter
        self.gender = gender
        if gender == "M":
            self.name = "John Doe"
        else:
            self.name = "Jane Doe"

    def __str__(self):
        return str(self.index) + " : " + self.gender + " : " +\
               self.name


# Data file update
def update():
    # Write the updated bodies list to the data file
    import pickle
    with open(data_file, 'wb') as out_file:
        pickle.dump(bodies, out_file)


def init():
    global bodies, in_file
    # Does the data file exist?
    if os.path.isfile(data_file):
        # Yes, load the bodies list from the data file
        import pickle

        with open(data_file, "rb") as in_file:
            bodies = pickle.load(in_file)
    else:
        print(data_file, "does not exist")
        bodies = []


init()
