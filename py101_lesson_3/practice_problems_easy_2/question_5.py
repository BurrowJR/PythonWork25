# How would you verify whether the data structures assigned to
# the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
# isinstance() takes inheritance into account
print(isinstance(numbers, list))
print(isinstance(table, list))
print()
# type() does not take inheritance into account
print(type(numbers))
print(type(table))
