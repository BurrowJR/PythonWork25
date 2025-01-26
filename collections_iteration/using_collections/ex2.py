# Use slicing to write Python code to print a 6-character substring of "Launch School" that begins with the first c.

my_string = 'Launch School'
print(my_string)
print(my_string[4:10])
print(f'A 6-character substring of {my_string} is "{my_string[4:10]}"')



start = my_string.find('c')
print(my_string[start:start + 6])