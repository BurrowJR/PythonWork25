# Build a program that asks the user to enter the length and width
# of a room, in meters, then prints the room's area in both
# square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# user input l and w in meters
# print area in square meters and square feet

def prompt(message):
    return input(">>> " + message).strip()

def valid_input(message):
    while True:
        user_input = prompt(message)
        try:
            number = float(user_input)
            if number > 0:
                return number
            print("Error: Please enter a number greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def get_unit():
    while True:
        unit = prompt("Would you like to enter dimensions"
        " in meters or in feet? (m/f) ").lower()
        if unit in ["m", "f"]:
            return unit
        print("Error: Please enter 'm' for meters or 'f' for feet.")

unit_mapping = {"m": "meters", "f": "feet"}

def area_of_room():
    print("Welcome! Let's calculate the area of your room.")
    unit = get_unit()
    unit_name = unit_mapping[unit]

    length = valid_input(f"What is the length in {unit_name}? ")
    width = valid_input(f"What is the width in {unit_name}? ")

    area = length * width

    if unit == "m":
        area_in_meters = area
        area_in_feet = area * 10.7639
    else:
        area_in_meters = area / 10.7639
        area_in_feet = area

    print(f"\nRoom Area = {length} * {width}")
    print(f"--\033[4mSquare meters\033[0m : {area_in_meters:,.2f}")
    print(f"--\033[4mSquare feet\033[0m   : {area_in_feet:,.2f}")

area_of_room()