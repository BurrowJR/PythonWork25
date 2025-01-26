stuff = ('hello', 'world', 'bye', 'now')

print(stuff)
print(type(stuff))
my_list = list(stuff)
my_list[2] = 'goodbye'
print(my_list)
print(type(my_list))
stuff = tuple(my_list)
print(stuff)
print(type(stuff))

# tuples are immutable so I have to change stuff to a list, change the element "bye" at index 2 to 'goodbye', then change it back to a tuple. 
print()
print(stuff[0:2] + ('goodbye', stuff[3]))
# I could also use concatenation to slice the original tuple and then combine the changed element with index 3