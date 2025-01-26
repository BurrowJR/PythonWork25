my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
print()
for value in my_dict.values():  # must use .values() or it returns the keys 
    print(value)
print()
for item in my_dict.items():
    print(item)
print()
for key, value in my_dict.items():    # tuple unpacking
    print(f'{key} = {value}')
