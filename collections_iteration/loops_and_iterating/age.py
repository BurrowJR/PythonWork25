# The updated code should use a for loop to display the future ages.

current_age = input('How old are you? ')
print()
print(f'You are {current_age} years old.')

for years in range(10, 50, 10):
    future_age = int(current_age) + years
    print(f'In {years} years, you will be {future_age} years old.')
print()

