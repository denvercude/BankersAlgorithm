# Banker's Algorithm
# Author: Denver Cude
# Course: COMP 322
# Date: 11/01/24

# ----------------
# Global Variables
# ----------------
num_resources = 0
num_processes = 0
resource_units = []
max_claim = []
allocated = []
available = []
need = []
safe_sequence = []


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
    global num_processes
    num_processes = int(input("Enter the number of processes: "))
    global num_resources
    num_resources = int(input("Enter the number of resources: "))

    # Allocate memory for resource, available, max_claim, allocated, and need arrays
    user_input = input(f"Enter number of units for resources (r0 to r{num_resources - 1}): ")
    global resource_units
    resource_units = list(map(int, user_input.split()))

    global max_claim
    max_claim = []
    for i in range(num_processes):
        user_input = input(f"Enter maximum number of units process p{i} will request from each resource (r0 to r{num_resources - 1}): ")
        row = list(map(int, user_input.split()))
        max_claim.append(row)

    global allocated
    allocated = []
    for i in range(num_processes):
        user_input = input(f"Enter number of units of each resource (r0 to r{num_resources - 1}) allocated to process p{i}: ")
        row = list(map(int, user_input.split()))
        allocated.append(row)
    
    global available
    available = []
    for j in range(num_resources):
        allocated_sum = sum(allocated[i][j] for i in range(num_processes))
        available.append(resource_units[j] - allocated_sum)

    global need
    need = [[0] * num_resources for _ in range(num_processes)]
    for i in range(num_processes):
        for j in range(num_resources):
            need[i][j] = max_claim[i][j] - allocated[i][j]

def determine_safe_sequence():
    
    global safe_sequence
    safe_sequence = []

    
    finished = [False] * num_processes

    
    progress = True

   
    while len(safe_sequence) < num_processes and progress:
        
        progress = False

        
        for i in range(num_processes):
            if not finished[i]:
                
                print("Checking: < ", end='')
                for j in range(num_resources):
                    print(f"{need[i][j]} ", end='')
                print("> <= < ", end='')
                for j in range(num_resources):
                    print(f"{available[j]} ", end='')
                print("> :", end='')

                can_run = True
                for j in range(num_resources):
                    if need[i][j] > available[j]:
                        can_run = False
                        break

                
                if can_run:
                    print(f"p{i} safely sequenced")
                    for j in range(num_resources):
                        available[j] += allocated[i][j]
                    safe_sequence.append(i)
                    finished[i] = True
                    progress = True
                else:
                    print(f"p{i} could not be sequenced")

def print_resource_available():
    # Print Units/Available Table
    print(f"\tUnits   Available")
    print(f"{'-' * 24}")
    for i in range(num_resources):
        print(f"r{i}\t{resource_units[i]}\t{available[i]}")

def print_matrix():
    resource_headers = ""
    for i in range(num_resources):
        resource_headers += f"r{i}"
        resource_headers += "\t"

    # Print headers, each centered within a 30-character block
    print(f"\tMax claim\t\t\tCurrent\t\t\t\tPotential")
    print(f"\t{resource_headers}\t{resource_headers}\t{resource_headers}")
    print('-' * 90)

    for i in range(num_processes):
        max_claim_string = ""
        for j in range(num_resources):
            max_claim_string += f"{max_claim[i][j]}"
            max_claim_string += "\t"
        
        current_string = ""
        for j in range(num_resources):
            current_string += f"{allocated[i][j]}"
            current_string += "\t"
        
        potential_string = ""
        for j in range(num_resources):
            potential_string += f"{need[i][j]}"
            potential_string += "\t"
        
        print(f"p{i}\t{max_claim_string}\t{current_string}\t{potential_string}")


# ------------------
# Main Program Logic
# ------------------~

# Get the initial selection
selection = get_menu_choice()

while 0 < selection < 3:
    if selection == 1:
        enter_parameters()
        print()
        print_resource_available()
        print()
        print_matrix()
        print()
        selection = get_menu_choice()
    else:
        determine_safe_sequence()
        print()
        selection = get_menu_choice()

print("Quitting program...")