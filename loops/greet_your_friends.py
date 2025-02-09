# Your friends just showed up! Given the following list of names, use a 'for' loop to greet each friend individually.

friends = ['Sarah', 'John', 'Hannah', 'Dave']

for friend in friends:
    print(f'Hello, {friend}')

# On line 3 the 'friends' variable is initialized with a list of names.
# On line 5 the 'for' loop is initialized iterating over a sequence of items (a list of names in the variable 'friends').
# On line 6, inside the loop, the 'print' function uses an f-string to print out 'Hello, {friend}' ; replacing '{friend}' with each name in the list on each iteration of the loop to the console.