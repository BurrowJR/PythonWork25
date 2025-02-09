# What happens if we take the list ['fish', 'and', 'chips'] and try to access the element at index position 10?
# First try to determine what will happen by consulting the documentation, then verity your understanding in the Python REPL.

lunch = ['fish', 'and', 'chips']

# print(lunch[10]) IndexError: list index out of range

length_of_lunch = (len(lunch))
print(f'index will be 1 less than the length: {length_of_lunch}')
[print('Index is 0 based (0, 1, 2), length gives the number of elements(1, 2, 3)')]