# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1) # dict() creates a new dictionary, however the list is a shallow copy of the original list meaning the list will reference the same list object as the original.
dict1['a'][1] = 42  # This will mutate both dictionaries
print(dict2['a'])   # [1, 42, 3]
print(dict1['a'])