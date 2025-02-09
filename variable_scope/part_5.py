a = 1

def my_function():
    print(a)
    a = 2    # can not change or reassign value when it was initialized outside the function.

my_function()  # UnboundLocalError: cannot access local variable 'a where it tis not associated with a value.
