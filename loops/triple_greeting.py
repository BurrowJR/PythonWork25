# Write a loop that prints the value of the greeting variable three times.

greeting = 'Aloha!'

# for loop
for _ in range(3):
    print(greeting)

# On line 3 we initialize the variable 'greeting' to 'Aloha!'
# On line 6 a 'for' loop is initialized to iterate over a sequence of numbers in 'range(3)'. The 'range(3)' function generates a sequence of numbers starting from 0 to 3 (exclusive); generating the numbers 0, 1, 2.
# On line 7, inside the loop, a 'print(greeting)' statement output 'greeting' for each iteration to the console.

# while loop
count = 0

while count < 3:
    print(greeting)
    count += 1

# On line 3 the variable 'greeting' is initialized to 'Aloha!'
# On line 14 the variable 'count' is initialized to 0. This variable will be used as a counter to keep track of the number of iterations.
# On line 16 the 'while' loop is initialized and will run as long as the condition 'count < 3' is truthy.  Meaning the loop will execute three times.
# On line 17, inside the loop, the 'print(greeting)' statement outputs the value of the greeting variable to the console. This happens for each iteration of the loop. 
# On line 18 the 'count' variable is incremented by '1' using the 'count += 1' statement. This ensures that the loop will terminate when 'count' reaches '3'.