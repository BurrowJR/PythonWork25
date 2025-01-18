def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# This code will print 42, 3, 2,
# foo was defined with 3 parameters first, second, third, in which default values were set for second and third.
# foo was invocated with 1 argument and Python uses the 2 default values for the 2nd and 3rd arguments.