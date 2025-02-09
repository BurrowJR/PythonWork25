# Using the code below as a starting point, write a 'while' loop that prints the elements of 'lst' at each index and terminates after printing the last element of the list.

lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

# On line 3 the variable 'lst' is initialized with the value of '[1, 3, 7, 15]'.
# On line 4 the variable index is initialized with the value of '0'. And will be used as a counter to keep track of the number of iterations.
# On line 6 the 'while' loop is initialized and will run as long as the condition of 'index < len(lst)' is truthy. Meaning as long as the index count is less than the length of the 'lst' elements.
# On line 7, inside the loop, the 'print(lst[index])' statement will print the current index element of 'lst' to the console for each iteration of the loop.
# On line 8 'index' is incremented by 1 with the 'index += 1' statement.

# If the 'lst' variable was empty nothing would print to the console, because there is nothing to print.