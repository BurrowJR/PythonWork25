def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

'''
 Identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

 function names: multiply()  defined on line 1 and used on line 9
                 get_num() defined on line 4 and used on lines 7 and 8
                 float built-in function used on line 5
                 input built-in function used on line 5
                 print built-in function used on line 10
parameters: left defined on line 1 and used as a local variable on line 2
            right defined on line 1 and used as a local variable on line 2
            prompt defined on line 4 and used as a local variable on line 5
 '''