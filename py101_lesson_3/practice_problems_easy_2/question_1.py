numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
# Write two distinct ways of reversing the list
# without mutating the original list.

# slicing can reverse the list
print(numbers[-1::-1])
print(numbers)
print()
# reversed() can reverse the list but returns a lazy sequence (an iterator)
# the iterator must be converted into a list
print(list(reversed(numbers)))
print(numbers)
# something to remember-- reversed() returns a lazy sequence
# .reverse()  mutates the original list
# numbers.reverse()  ---- mutates
print()
# a new variable can be created and the list reversed with a for loop
reversed_numbers = []
for num in numbers:
    reversed_numbers.insert(0, num)
print(reversed_numbers)
print(numbers)