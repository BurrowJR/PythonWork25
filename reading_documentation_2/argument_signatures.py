# How many arguments does the str.join() method expect? What happens if you call it with fewer or more arguments?

print('The str.join() method is used to concatenate a sequence of strings with a specified separator.\nIt takes one argument, if no argument or more than one argument is given it will return a TypeError.')
print()
#  separator.join(iterable)

greeting = ['Hello', 'How', 'are', 'you', '?']
my_list = ['Such', 'a', 'good', 'dog', '.']
print('< >'.join(greeting))
# print('< >'.join(greeting, my_list))  
# TypeError: str.join() takes exactly one argument (2 given)
print()
# print('< >'.join())
# TypeError: str.join() takes exactly one argument (0 given)
