# Without running the following code, what values will be printed by line 10?

pets = {'Cat': 'Meow',
        'Dog': 'Bark',
        'Bird': 'Tweet',
        }

keys = pets.keys()   # returns a dictionary view object,  contains just the keys
print(keys)
del pets['Dog']      # this deletes the key 'Dog' and its value
print(keys)
pets['Snake'] = 'Sssss' # adds the key 'Snake' with a value of 'Sssss'
print(keys)    # dict_keys(['Cat', 'Bird', 'Snake'])

values = pets.values()
items = pets.items()
print()
print(values)
print(items)
print()
lst_pets = zip(keys, values)
print(list(lst_pets))