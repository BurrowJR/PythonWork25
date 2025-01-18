def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(remainders_3(numbers_1))
print(remainders_3(numbers_2))
print(remainders_3(numbers_3))
print(remainders_3(numbers_4))
print()
# This function takes a list of numbers and returns a new list containing the remainders when each number is divided by 3. The list comprehension iterates over each number in the input list and calculates the remainder using the modulo operator.

# To me this code is easier to read:

def remainders_4(numbers):
    remainders = []
    for number in numbers:
        (remainders.append(number % 4))
    return remainders

numbers = [10, 15, 21, 33, 42]
remainders = remainders_4(numbers)
print(remainders)
print(any(remainders))
print()
'''
To use this function to determine which of the following lists contain at least one number that is not evenly divisible by 3 (that is, the remainder is not 0, 0 being falsy) we can use the any() function.  The any() function returns True if any element of the iterable is true and False if any element is falsy or empty.
'''

print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))
