def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

#find_first_nonzero_among(0, 0, 1, 0, 2, 0) # TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given
#find_first_nonzero_among(1) # TypeError: 'int' object is not iterable

print(find_first_nonzero_among([0, 0, 1, 0, 2, 0]))
print(find_first_nonzero_among([1]))
