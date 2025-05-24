def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_func = counter()
print(counter_func())  # Output: 1
print(counter_func())  # Output: 2
print(counter_func())  # Output: 3
print(counter_func())  # Output: 4
print(counter_func())  # Output: 5
print(counter_func())  # Output: 6
print(counter_func())  # Output: 7
