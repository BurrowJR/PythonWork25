my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
print(my_list == another_list)
# my_list and another_list are equal they contain the same elements
print(my_list is another_list)
# my_list and another_list are not the same object they are in different places in memory; the list constructor function creates a new object
print(my_list[3] == another_list[3])
# yes they are equal; they have the same elements
print(my_list[3] is another_list[3])
# Nested lists hold the same place in memory so yes they are the same object for the nested list; the list constructor function only copies the reference to the nested list not the actual list; shallow copy