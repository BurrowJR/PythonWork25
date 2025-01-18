def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# This will print 42, 3.141592, 2
# foo was defined with 3 parameters with second and third assigned default values. foo() was called with 2 arguments and Python uses the third default value of 2.