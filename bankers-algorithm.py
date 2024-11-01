# Banker's Algorithm
# Author: Denver Cude
# Course: COMP 322
# Date: 11/01/24

# -------
# Imports
# -------

# -------
# Classes
# -------

# ---------
# Functions
# ---------

def get_menu_choice():
    menu_selection = 0
    print("Banker's Algorithm")
    print("------------------")
    print("1) Enter parameters")
    print("2) Determine safe sequence")
    print("3) Quit program")
    print()
    menu_selection = int(input("Enter selection: "))
    return menu_selection

# ------------------
# Main Program Logic
# ------------------

# Get the initial selection
selection = get_menu_choice()

while 0 < selection < 3:
    if selection == 1:
        print("Selection is 1.")
        print()
        selection = get_menu_choice()
    if selection == 2:
        print("Selection is 2.")
        print()
        selection = get_menu_choice()

