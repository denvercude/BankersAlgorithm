# Banker's Algorithm
# Author: Denver Cude
# Course: COMP 322
# Date: 11/01/24

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

def print_resource_vector():
    # Loop through each resource index
    # Print total units and available units for each resource
    pass

def print_matrix():
    # Loop through each resource index
    # For each process and resource, print:
    # - Max number of units each process may request
    # - Units allocated
    # - Units needed
    pass

def enter_parameters():
    # Get the number of processes and resources.
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of processes"))

    # Allocate memory for resource, available, max_claim, allocated, and need arrays
    resource = [0] * num_resources
    available = [0] * num_resources
    max_claim = []
    for i in range(num_processes):
        row = [0] * num_resources
        max_claim.append(row)
    allocated = []
    for i in range(num_processes):
        row = [0] * num_resources
        allocated.append(row)
    need = []
    for i in range(num_processes):
        row = [0] * num_resources
        need.append(row)
    pass

def determine_safe_sequence():
    # While not all processes are sequenced:
    # - For each process, if not yet safely sequenced:
    #     - For each resource, check if need <= available
    #     - If all resources are available, safely sequence process
    #     - Update available resources and free resources allocated to the process
    #     - Increment number of sequenced processes
    pass

def quit_program():
    # Check if vectors/arrays are not None; if so, free each vector/array
    pass

# ------------------
# Main Program Logic
# ------------------

# Get the initial selection
selection = get_menu_choice()

while 0 < selection < 3:
    if selection == 1:
        enter_parameters()
        print()
        selection = get_menu_choice()
    elif selection == 2:
        determine_safe_sequence()
        print()
        selection = get_menu_choice()
    elif selection == 3:
        quit_program()
