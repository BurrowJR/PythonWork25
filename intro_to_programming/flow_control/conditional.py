value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    pass  # We don't car about 9
else:
    print('value is something else')
print()
def truthy_or_falsy(value):
    if value:
        print(f'{value} is truthy')
    else:
        print(f'{value} is falsy')

truthy_or_falsy(5)
truthy_or_falsy(0)
truthy_or_falsy(22)
truthy_or_falsy(-3)
truthy_or_falsy('hello')
truthy_or_falsy('')
truthy_or_falsy([])
truthy_or_falsy([1, 2, 3])
print()

foo = None        # sets foo to False
bar = 'qux'       # sets bar to True
is_ok = foo or bar
print(is_ok)
print()

if foo or bar:
    is_ok = True
else:
    is_ok = False
print(bar)
print(foo)
print()

bar = None
foo = 'qux'
is_ok = bool(foo or bar)
print(foo)
print(bar)