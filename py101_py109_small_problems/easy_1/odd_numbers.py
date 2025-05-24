# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# odd numbers 1-100
for number in range(101):
    if number % 2 != 0:
        print(number)
print()

print(*(number for number in range(1, 100, 2) if number % 2 != 0), sep="\n")