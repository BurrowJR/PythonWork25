obj = 42                       # assigning the variable
print(obj)
obj = 'ABcd'                   # reassigned
print(obj)
print(obj.upper())             # neither returns the object in upper case 
obj = obj.lower()              # reassigned
print(obj)
print(len(obj))                # neither returns the number of characters 4
obj = list(obj)                # reassigned
print(obj)
print(obj.pop())               # mutated removes the element at the last index
obj[2] = 'X'                   # mutated changes the element at index 2 to 'X'
print(obj)
obj.sort()                     # mutated returns a list in ascending order 
print(obj)
print(set(obj))                # neither returns object as a set
obj = tuple(obj)               # reassigned
print(obj)