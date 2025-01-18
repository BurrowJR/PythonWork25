def multiply(num1, num2):
    result = num1 * num2
    return result

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

product = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {product}')


