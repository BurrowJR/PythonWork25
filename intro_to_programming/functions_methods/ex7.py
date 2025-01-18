def foo(bar, qux):  # Defined foo() with 2 parameters
    print(bar)
    print(qux)

#foo('Hello')  # Only 1 argument given
foo('Hello', 'Goodbye')  # A second parameter is given to fix this error

# This code will raise an error:  TypeError: foo() missing 1 required positional argument: 'qux'