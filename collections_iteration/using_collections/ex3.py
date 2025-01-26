# Write Python code to create a new tuple from (1, 2, 3, 4, 5).  The new tuple should be in reverse order from the original.  It should also exclude the first and last members of the original.  The result should be the tuple (4, 3, 2)

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
my_list.pop()
my_list.pop(0)
new_tuple = tuple(my_list)

print(new_tuple)
print(f'This is the new tuple using the reverse and pop methods: {new_tuple}')
print()

lst = list(my_tuple)
lst.reverse()
new_tuple2 = tuple(lst[1:4])
print(f'This is the new tuple using the reverse method and slicing: {new_tuple2}')