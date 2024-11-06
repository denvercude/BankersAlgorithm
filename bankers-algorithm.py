# Banker's Algorithm
# Author: Denver Cude
# Course: COMP 322
# Date: 11/01/24

# ----------------
# Global Variables
# ----------------
num_resources = 0

resource_array = []
available = []


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

def enter_parameters():
    # Get the number of processes and resources.
    num_processes = int(input("Enter the number of processes: "))
    global num_resources
    num_resources = int(input("Enter the number of resources: "))

    # Allocate memory for resource, available, max_claim, allocated, and need arrays
    user_input = input(f"Enter number of units for resources (r0 to r{num_resources - 1}): ")
    global resource_array
    resource_array = list(map(int, user_input.split()))

    max_claim = []
    for i in range(num_processes):
        user_input = input(f"Enter maximum number of units process p{i} will request from each resource (r0 to r{num_resources - 1}): ")
        row = list(map(int, user_input.split()))
        max_claim.append(row)

    allocated = []
    for i in range(num_processes):
        user_input = input(f"Enter number of units of each resource (r0 to r{num_resources - 1}) allocated to process p{i}: ")
        row = list(map(int, user_input.split()))
        allocated.append(row)
    
    global available
    available = []
    for j in range(num_resources):
        allocated_sum = sum(allocated[i][j] for i in range(num_processes))
        available.append(resource_array[j] - allocated_sum)

def determine_safe_sequence():
    # While not all processes are sequenced:
    # - For each process, if not yet safely sequenced:
    #     - For each resource, check if need <= available
    #     - If all resources are available, safely sequence process
    #     - Update available resources and free resources allocated to the process
    #     - Increment number of sequenced processes
    pass

def print_resource_vector():
    # Print Units/Available Table
    print(f"{'':<8}{'Units':<8}{'Available':<9}")
    print(f"{'-' * 24}")
    for i in range(num_resources):
        print(f"r{i:<7}{resource_array[i]:<8}{available[i]:<8}")

def print_matrix():
    # Loop through each resource index
    # For each process and resource, print:
    # - Max number of units each process may request
    # - Units allocated
    # - Units needed
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
        print_resource_vector()
        print()
        selection = get_menu_choice()
    elif selection == 2:
        determine_safe_sequence()
        print()
        selection = get_menu_choice()
    elif selection == 3:
        quit_program()
