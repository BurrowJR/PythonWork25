def prompt_user_loan_amount(prompt):
    while True:
        loan_amount = (input(prompt))
        if not loan_amount.isdigit():
            print("Invalid input. Please enter a positive number.")
            continue
        loan_amount = float(loan_amount)
        if loan_amount <= 0:
            print("Value must be positive.")
            continue
        return loan_amount

def prompt_user_apr(prompt):
    while True:
        try:
            interest_rate = float(input(prompt))
            if 0 < interest_rate < 1:
                return interest_rate
            else:
                print("Please enter as a  positive decimal. " \
                "For example, 5% as .05.")
        except ValueError:
            print("Invalid input. Please enter a positive decimal number.")

def prompt_user_loan_duration(prompt):
    while True:
        try:
            loan_duration = int(input(prompt))
            if loan_duration <= 0:
                print("Value must be positive.")
                continue
            return loan_duration
        except ValueError:
            print("Invalid input. Please enter a positive number.")

print(">>>> Welcome to the Loan Calculator! <<<<")
loan_amount = prompt_user_loan_amount(">>>Enter the loan amount: ")
apr = prompt_user_apr(">>>Enter the annual percentage rate (APR) as a decimal: ")
loan_duration_months = prompt_user_loan_duration \
                      (">>>Enter the loan duration in months: ")

monthly_interest_rate = apr / 12
print(f"Your monthly interest rate will be: {monthly_interest_rate:.5f}")

monthly_payment = ( loan_amount * (monthly_interest_rate /
                  (1 - ( 1 + monthly_interest_rate) **
                  (-loan_duration_months))))

print(f"Your monthly payment will be: ${monthly_payment:.2f}")

total_payment = monthly_payment * loan_duration_months
print(f"Your total payment will be: ${total_payment:.2f}")