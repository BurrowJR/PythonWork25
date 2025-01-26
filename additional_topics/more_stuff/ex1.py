# What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl': 108,
    'Clare': 175,
    'Karis': 140,
    'Trevor': 180,
    'Antonina': 132,
    'Chris': 101,
}

print(do_something(my_dict))   # CHRIS


# When the do_something(dictionary) function is called on line 15 the my_dict dictionary is sorted in alphabetic order and then the key at index 1 is printed out in upper case letters.