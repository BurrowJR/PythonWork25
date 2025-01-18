def foo(bar, qux):
    print(bar)
    print(qux)

#foo(42, 3.141592, 2.718)  Will raise an error with 3 arguments
foo(42, 3.141592)

# This code will raise an error 2 parameters are defined, but 3 arguments are passed.   TypeError: foo() takes 2 positional arguments but 3 were given