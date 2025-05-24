# What does the last line in the following code output?

dictionary = {'first': [1]}    # dict are mutable
num_list = dictionary['first']  # only pointing to the list [1] not the key
print(type(num_list))
num_list.append(2)  # [1, 2]

# dictionary = {"first": [1]}
# num_list = dictionary["first"].copy()
# num_list.append(2)

# dictionary = {"first": [1]}
# num_list = dictionary["first"][:]
# num_list.append(2)

print(num_list)    # [1, 2]
print(dictionary)  #  {'first': [1, 2]}