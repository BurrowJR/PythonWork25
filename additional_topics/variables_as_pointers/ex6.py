# The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of dict1. Be careful: your're not allowed to use the copy module in this exercise.

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2)           # False
print(dict1['a']    is dict2['a'])      #  The rest are True
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

print()
