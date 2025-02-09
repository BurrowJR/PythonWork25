def find_maximum(numbers):
    if not numbers:
        return None
    
    max_number = numbers[0] # or float('-inf') negative infinity

    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))
print(find_maximum([-1, 0, 5, 3]))
print(find_maximum([-10, -3, -20, -2]))
print(find_maximum([]))    