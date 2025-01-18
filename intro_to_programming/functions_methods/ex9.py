def foo(first, second=3, third=2):   # 3 parameters are defined with second and third having default values, meaning this code will work properly with 1, 2, or 3 arguments given.
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)
print()
foo(42)
print()
foo(42, 3.141592)
#foo()  TypeError: foo() missing 1 required positional argument: 'first'
#foo(1, 2, 3, 4)  TypeError: foo() takes form 1 to 3 positional arguments but 4 were given

# This code will print 42, 3.141592, 2.718.