# The following code will raise an error because it has a decimal, it is a float not an integer.
# print(int('3.1415'))  ValueError: invalid literal for int() with base 10; '3.1415'
print(float('3.1415'))
string = '3.1415'
float = float(string)
integer = int(float)

print(f'This is a string: {repr(string)}.')
print(f'This is a float: {float}.')
print(f'This is an integer: {integer}.')   