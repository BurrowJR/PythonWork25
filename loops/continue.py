# Write a 'for' loop that iterates over the elements of the list 'cities' and prints the length of each string. If the element is 'None', use the 'continue' statement to skip forward to the next iteration without printing anything.

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None, 'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city == None:
        continue
    print(len(city))
 
# Line 3 the variable 'cities' is initiated with a list of values.
# Line 5 initializes a 'for' loop to iterates over each element in the 'cities' list.
# Line 6 uses an 'if' statement inside the loop to check if the current element in 'city' is 'None'.  'if city == None' If it is truthy, the 'continue' statement is executed, (line 7) skipping the rest of the loop and moves to the next iteration.
# Line 8 if the current element is falsy, not equal to 'None', the 'print(len(city)) statement is executed, printing the length of the current element 'city'.