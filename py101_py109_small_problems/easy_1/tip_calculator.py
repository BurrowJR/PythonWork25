print("Welcome to the tip calculator.")
print("--" * 15)

def get_valid_number(prompt):
    while True:
        try:
            value = float(input(f">> {prompt} ").strip())
            if value > 0:
                return value
            print("Error: Please enter a number greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")
            
bill = get_valid_number("Please enter the bill amount. ($):")
tip = get_valid_number("Please enter the tip percentage\n(e.g., enter 10 for 10%:")

tip_amount = bill * (tip / 100)
bill_total = bill + tip_amount

print("\nTip Calculation Summary:")
print(f"{'Bill amount:':<20} ${bill:>10,.2f}")
print(f"{'Tip amount:':<20} $\033[4m({tip_amount:>9,.2f})\033[0m")
print(f"{'Total bill amount:':<20} ${bill_total:>10,.2f}")