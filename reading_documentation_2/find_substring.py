print('Using the official Python documentation, can you determine how to check whether a string\ncontains a specific substring?')

my_string = 'Charlotte is such a good dog.'

print('Charlotte' in my_string)
print('The in keyword determines if a substring is present within a string and returns a boolean\nof True or False.')
print()
print(my_string.find('Charlotte'))
print('The str.find() also determines if a substring is present within a string and returns the index\nof the substring.')