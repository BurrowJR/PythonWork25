def multiply(num1, num2):
    result = num1 * num2
    return result

print(multiply(5, 3) == 15)  # True

def square(num):
    return multiply(num, num)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

def power(num, n):
    result = 1
    for _ in range(n):
        result = multiply(result, num)
    return result

print(power(2, 3))
print(power(5, 2))
print(power(4, 3))