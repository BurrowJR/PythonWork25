# Programmatically determine whether 42 lies between 10 and 100, inclusive.
# Do the same for the values 100 and 101.

def find_number(number):
    if number in range(10, 101):
        print(f"{number} is between 10 and 100.")
    else:
        print(f"{number} is NOT between 10 and 100.")

find_number(42)
find_number(100)     
find_number(101)
find_number(9)       
find_number(10)       
