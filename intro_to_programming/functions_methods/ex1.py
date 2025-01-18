def set_foo():
    foo = 'bar'
    print(foo)

set_foo()
# print(foo) foo is out of scope.
print(f'foo {set_foo()}')  

# The program outputs an error: NameError: name 'foo' is not defined
# We get this result because foo is out of scope; foo is only accessible from within the set_foo() function.