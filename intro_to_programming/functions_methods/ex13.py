def foo(first, third, second=3):
#def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

#foo(42)
foo(42, 35)

# This code will raise an error
# SyntaxError: parameter without a default follows parameter with a default
# In Python you can not have a non-default parameter following a default parameter.