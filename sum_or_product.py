def calculate_sum_or_product():
    while True:
        try:
            number = int(input("Enter an integer greater than 0:  "))
            if number > 0:
                break
            else:
                print("The number must be greater than 0. Please try again.")
        except ValueError:
            print("That's not a valid integer. Please try again.")
    
    while True:
        choice = input("Do you want to calculate the sum or the product of all "
                    f"numbers between 1 and {number}?\n"
                     "(Enter 'sum' or 'product'):  ").strip().lower()
        if choice in ('sum', 'product'):
            break
        else:
            print("Invalid choice. Please enter 'sum' or 'product.")
    if choice == 'sum':
        result = sum(range(1, number + 1))
        print(f"The sum of all numbers between 1 and {number} is {result}.")
    elif choice == 'product':
        result = 1
        for i in range(1, number + 1):
            result *= i
        print(f"The product of all numbers between 1 and {number} is {result}.")

calculate_sum_or_product()