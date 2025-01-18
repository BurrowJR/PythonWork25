# Classify the identifiers as global, local, or built-in.

def multiply(left, right):   # multiply is a global function identifier
    return left * right      # left and right are local parameter identifiers 
                             # to the multiply function 
                             # (return is a key word)


def get_num(prompt):             # get_num is a global function identifier
    return float(input(prompt))  # prompt is a local identifier to the
                                 # get_num function
                                 # float and input are built-in global functions

first_number = get_num('Enter the first number: ')       # first_number is a
                                                         # global identifier

second_number = get_num('Enter the second number: ')     # second_number is a
                                                         # global identifier

product = multiply(first_number, second_number)          # product is a 
                                                         # global identifier

print(f'{first_number} * {second_number} = {product}')   # print is a global
                                                         # built-in function
