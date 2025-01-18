def compound_interest(principal, rate, times_compounded, years):
    balance = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    return balance

principal = 1000
rate = 0.05
times_compounded = 1
years = 5

balance = compound_interest(principal, rate, times_compounded, years)

print(f"Your balance after {years} years is:  ${balance:.2f}")

print()
balance2 = (1000 * (1.05**5))
print(balance2)