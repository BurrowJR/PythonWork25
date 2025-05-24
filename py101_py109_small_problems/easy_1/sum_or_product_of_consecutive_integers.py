print("Welcome to Sum or Product!")
print('**' * 15)
print("Here we will be either adding or multiplying all of the numbers\n" \
"between 1 and the number you enter.")
print("Let's get started!\n")

def get_valid_number(prompt):
    while True:
        try:
            number = int(input(f">>> {prompt} ").strip())
            if number > 0:
                return number
            print("Error: Please enter a whole number greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def get_valid_operation(prompt):
    while True:
        try:
            operation = input(f">>> {prompt} ").strip().lower()
            if operation in ['s', 'p']:
                return operation
            print("Error: Please enter 's' for sum or 'p' for product.")
        except ValueError:
            print("Error: Invalid input. Please enter 's' for sum or 'p' for product.")

def get_valid_go_again(prompt):
    while True:
        try:
            go_again = input(f">>> {prompt} ").strip().lower()
            if go_again in ['y', 'n']:
                return go_again
            print("Error: Please enter 'y' to play again or 'n' to exit.")
        except ValueError:
            print("Error: Invalid input. Please enter 'y' or 'n'.")

while True:

    number = get_valid_number("Please enter a whole number greater than 0: ")
    operation = get_valid_operation("Enter 's' to compute the sum, or 'p' to compute the product.")

    if operation == 's':
        total = sum(range(1, number + 1))
        print(f"\nThe sum of the integers between 1 and {number} is {total:,}.")
    elif operation == 'p':
        product = 1
        for i in range(1, number + 1):
            product *= i
        print(f"\nThe product of the integers between 1 and {number} is {product:,}.")
    again = ()

    go_again = get_valid_go_again("Would you like another calculation? 'y' for yes 'n' for no.")

    if go_again == 'y':
        print("Another calculation coming right up!")
    else:
        print("Have a nice day, thanks for stopping by!")
        break
