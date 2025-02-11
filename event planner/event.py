guest_list = []

# add Guest to the list function
def add_guest(guest_list, guest_name):
    guest_list.append(guest_name)
    # print(f"{guest_name} has been added to the list")


# Display guest function
def display_guest(guest_list):
    if not guest_list:
        print("Guest list is empty")
        return
    print("GUEST LIST:")
    for i,guest in enumerate(guest_list, start=1):
        print(f"{i}: {guest}")

# Function to calculate the total cost of the event
def calculate_cost(event_type, num_guests):
    event_costs = {
        "wedding": {"per_guest": 100, "flat_fee": 500},
        "conference": {"per_guest": 50, "flat_fee": 300},
        "birthday": {"per_guest": 20, "flat_fee": 100}
    }
    
    if event_type not in event_costs:
        return "Invalid event type. Please choose wedding, conference, or birthday."
    
    # Extract costs
    costs = event_costs[event_type]
    total_cost = num_guests * costs["per_guest"] + costs["flat_fee"]
    return total_cost


# Main Program
guest_list = []

n = int(input("Please enter how many guests you want to add?: "))
for i in range(n):
    variable = input("Enter your name: ")
    add_guest(guest_list, variable)


num_guests = len(guest_list)
for event in ["wedding", "conference", "birthday", "concert"]:
    cost = calculate_cost(event, num_guests)
    if isinstance(cost, str):  # Handle invalid event types
        print(f"Event Type: {event} - {cost}")
    else:
        print(f"Event Type: {event.capitalize()}, Total Cost: ${cost}")
# Displaying the guest list
display_guest(guest_list)

calculate_cost("birthday",num_guests)

# Calculating and displaying costs for different event types






