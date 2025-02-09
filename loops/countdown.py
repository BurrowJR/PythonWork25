# The following code prints the numbers from 1 to 10. Modify it so that it instead prints the numbers form 10 to 1 in descending order, followed by 'Launch!'.

for i in range(10, 0, -1):
    print(i)
    
print('Launch!')

# On line 3 a 'for' loop is initialized to iterate over a sequence of numbers in 'range(10, 0, -1)'.  The 'range' function generates a sequence of numbers starting at 10 in descending order to 0 (exclusive) with a step of -1, generating the numbers 10, 9, 8, 7, 6, 5, 4, 3, 2, 1.
# On line 4 inside the loop, the 'print(i)' statement outputs the current value of 'i' to the console for each iteration of the loop.
# One line 6 the 'print('Launch!') statement is executed once the loop has finished iterating through the 'range' function and prints the string 'Launch!' to the console.