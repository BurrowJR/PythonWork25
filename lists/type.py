some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

def is_list(variable):
    return isinstance(variable, list)

print(is_list(some_value1))
print(is_list(some_value2))

print()

print(isinstance(some_value1, list))
print(isinstance(some_value2, tuple))
print(isinstance(some_value2, str))