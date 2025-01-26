# Write a function called increment_counter that increments a counter variable every time it is called. You can test your code with the following:

counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

print(counter)

increment_counter()
print(counter)

increment_counter()
print(counter)

counter = 100
increment_counter()
print(counter)