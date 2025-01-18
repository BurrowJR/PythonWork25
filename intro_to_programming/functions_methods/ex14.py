# Identify all of the identifiers on each line of the following code.

def multiply(left, right):   # multiply, left, and right
    return left * right      # left and right

def get_num(prompt):               # get_num and prompt
    return float(input(prompt))    # float, input, and prompt

first_number = get_num('Enter the first number: ')      # first_number, get_num
second_number = get_num('Enter the second number: ')    # second_number, get_num
product = multiply(first_number, second_number)         # product, multiply, first_number, and second_number
print(f'{first_number} * {second_number} = {product}')  # print, first_number, second_number, and product

# float, input, and print are functions they are just defined in Python making them identifiers

# key words -- def, return,
# string literal -- 'Enter the first number: ' and 'Enter the second number: '