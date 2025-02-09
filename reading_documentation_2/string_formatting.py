name = 'Victor'
profession = 'programmer'

#  1. How can you print the string Hello, Victor. You are a programmer. using the str.format method? You should fill in the name and profession in a string literal that contains the rest of the text.

string_format = 'Hello, {}. You are a {}.'
greeting = string_format.format(name, profession)
print(greeting)
# or
print('Hello, {}. You are a {}.'.format(name, profession))

#  2. How can you achieve the same result using an f-string?

print(f'Hello, {name}. You are a {profession}.')

# Could also use string concatenation.

print('Hello, ' + name + '. You are a ' + profession + '.')

