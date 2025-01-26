names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)

'''
The variable 'names' holds a list of names. We want to append each name, in uppercase, to the initially empty 'upper_names' list. Since list indexes are zero-based, we initialize an index variable with 0.

Next, we use a loop that executes as long as the number in 'index' is smaller than the length of the 'names' list.

Line 8 increments the index by 1 after each iteration, which ensures that 'index < len(names)' becomes falsy after the loop handles the last element.

Line 6 accesses the name stored at 'names[index]' and uses it to call 
str.upper. That method returns the name in uppercase, which we assign to 'upper_name'. It doesn't change the original name in the 'names' list.

Line 7 uses 'list.append' to append the latest uppercase name to the 'upper_names' list. Over the four iterations of the 'names' list, line 7 appends four uppercase names to 'upper_names', one per iteration, in the same order the loop processes them.

Notice that we initialized 'names', 'upper_names', and 'index' before the loop.  We don't want to initialize them inside the loop: they would get reset during every iteration. Basically, nothing would change.
'''

# for loop

names2 = ['Fred', 'George', 'Ron', 'Hermione']
upper_names2 = []

for name in names2:
    upper_name2 = name.upper()
    upper_names2.append(upper_name2)

print(upper_names2)