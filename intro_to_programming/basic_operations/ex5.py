# Yes, an error will occur if you try to access a list element with an index greater than or equal to the list's length because the list element is zero based meaning the elements start at zero, then 1 and so on, so the list elements are always one less then its length.
foo = ['a', 'b', 'c']
print(foo[0])
print(foo[1])
print(foo[2])
#print(foo[3])   IndexError: list index out of range
print(len(foo))