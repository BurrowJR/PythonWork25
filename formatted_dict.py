car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
    'year': 2003,
}

car['price'] = 10_000
#del car['mileage']
print(f"${car['price']:,}")
print(len(car))
print()

# Function to format values
def format_value(key, value):
    if key == 'mileage':
        return'{:,}'.format(value)
    elif key == 'price':
        return '${:,}'.format(value)
    return value

# Determine the width of the longest key
max_key_length = max(len(key) for key in car)
max_value_length = max(len(value) for value in car)

# Print the whole dictionary with formatted and aligned values
for key, value in car.items():
    formatted_key = key.ljust(max_key_length)
    formatted_value = str(format_value(key, value)).ljust(max_value_length)
    print(f'{formatted_key}:   {formatted_value}')

print()
print(car['price'])
print(car['mileage'])