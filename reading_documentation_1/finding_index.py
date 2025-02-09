# Python lists come with a variety of built-in methods that allow for common list manipulations. One such operation is determining the index of an item in the list.

fruits = ['apple', 'banana', 'cherry', 'peach', 'watermelon']
print(fruits)
print('How would you determine the index of the fruit "cherry" in this list?')
print()

#  list.index(x[, start[, end]])

cherry_index = fruits.index('cherry', 0, len(fruits))
print(f'"cherry" is at index {cherry_index}')

watermelon_index = fruits.index('watermelon')
print(f'"watermelon" is at index {watermelon_index}')

apple_index = fruits.index('apple')
print(f'"apple" is at index {apple_index}')
