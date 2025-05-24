# Write two different ways to remove all of the elements from the
# following list:

numbers = [1, 2, 3, 4]
print(numbers)
numbers.clear()
print(numbers)
print()

numbers = [1, 2, 3, 4]
print(numbers)
del numbers[:]
print(numbers)
print()

numbers = [1, 2, 3, 4]
print(numbers)
while numbers:
    numbers.pop()
print(numbers)
