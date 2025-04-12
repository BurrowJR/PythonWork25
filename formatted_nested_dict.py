vehicle = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'mileage': 80_000,
        'year': 2003,
        'price': 10_000,
    },
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'mileage': 145_500,
        'year': 1998,
        'price': 6_000,
    },
}

# Function to format values with conditional logic
def format_value(key, value):
    if key == 'mileage':
        return '{:,}'.format(value)
    elif key == 'price':
        return '$ {:,}'.format(value)
    else:
        return value

# Recursive function to format nested dictionary
def format_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            format_dict(value)
        else:
            d[key] = format_value(key, value)

# Format the nested dictionary
format_dict(vehicle)

# Determine the width of the longest key
def find_max_key_length(d, indent=0):
    max_length = 0 
    for key, value in d.items():
        max_length = max(max_length, len(key) + indent)
        if isinstance(value, dict):
            max_length = max(max_length, find_max_key_length(value, indent))
    return max_length

find_max_key_length = find_max_key_length(vehicle)

# Print the formatted nested dictionary
def print_formatted_dict(d, indent=0):
    for key, value in d.items():
        formatted_key = key.ljust(find_max_key_length + indent)
        if isinstance(value, dict):
            print()
            print(f"{formatted_key}:")
            print_formatted_dict(value, indent + 3)
        else:
            formatted_value = str(value).rjust(8)
            print(f'{' ' * indent}{formatted_key}: {formatted_value}')

print_formatted_dict(vehicle)
