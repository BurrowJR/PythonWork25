def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# This code will raise an error
# TypeError: foo() missing 1 required positional argument: 'first'
# At least 1 argument must be given because first does not have a default value assigned to it.