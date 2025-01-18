foo = 'bar'

def set_foo():
    foo = 'qux'
    print(f'This foo is in the local scope: {foo}')

set_foo()
print(f'This foo is in the global scope: {foo}')

# This program prints 'bar'.
# On line 1 the foo variable is set to bar in the outer scope giving us the output of 'bar'.
# The foo variable on line 4 is only accessible within the set_foo function. Thus, shadowing the foo variable on line 1 and does not change the value of foo outside of the function.
