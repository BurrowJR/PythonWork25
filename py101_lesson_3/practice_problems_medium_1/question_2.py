# Alan wrote the following function, which was intended
# to return all of the factors of number:

# original code
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# Simply change the != 0 to > 0
def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# validate by asking for a positive number
# def factors(number):
#     divisor = number
#     if number < 0:
#         print("Please enter a positive number")
#         return []

#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# validate by changing the negative number to positive with abs()
# def factors(number):
#     number = abs(number)
#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result


print(factors(4))
print(factors(5))
print(factors(-3))
print(factors(-4))
print(factors(20))

def prompt(message):
    return input(">>>" + message).strip().lower()
def factors():
    while True:
        try:
            number = int(prompt("Enter a positive number: "))

            if number < 0:
                choice = prompt("You entered a negative number." \
                "Convert to positive? y/n: ")
                if choice == "y":
                    number = abs(number)  # Turns input into a positive number
                else:
                    print("Please enter a positive number.")
                    continue
            break
        except ValueError:  # Makes sure a number is entered
            print("Invalid input! Please enter a positive number. ")
        
    divisor = number
    result = []

    while divisor != 0:
        if number % divisor == 0:  # Makes sure number is evenly divisible
            result.append(number // divisor)
        divisor -= 1
    return number, result

while True:
    number, result = factors()
    print(f"You entered: {number} and multiples of {number} are {result}")
    print()
    while True:
        another_number = prompt("Do you want to enter another number? y/n: ").strip().lower()
        if another_number in ("y", "n"):
            break
        print("Please enter 'y' or 'n'.")

    if another_number == "n":
        print("Have a nice day!")
        break