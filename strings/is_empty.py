def is_empty(string):
    return string == ''

print(is_empty('mars'))
print(is_empty(' '))
print(is_empty(''))

# or
print()

def is_empty(string):
    return len(string) == 0

print(is_empty('Hello'))
print(is_empty('   '))
print(is_empty(''))

# or
print()

def is_empty(string):
    return not string

print(is_empty(""))
print(is_empty('not'))