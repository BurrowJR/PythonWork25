number = 4936
ones_place = number % 10
print(f'{ones_place} is in the ones place in the number {number}.')
tens_place = number // 10 % 10
print(f'{tens_place} is in the tens place in the number {number}.')
hundreds_place = number // 100 % 10
print(f'{hundreds_place} is in the hundreds place in the number {number}.')
thousands_place = number // 1000
print(f'{thousands_place} is in the thousands place in the number {number}.')
print()
print(f'1. One place is {ones_place}.')
print(f'2. Tens place is {tens_place}.')
print(f'3. Hundreds place is {hundreds_place}.')
print(f'4. Thousands place is {thousands_place}.')
