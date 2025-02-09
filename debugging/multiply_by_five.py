def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input()) # Must be converted into an integer

print(f"The result is {multiply_by_five(number)}!")