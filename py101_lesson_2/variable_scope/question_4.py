# What will the following code print and why?
def outer():       # the outer function is defined with no parameters
    outer_var = 'Hello'  # a local variable outer_var is defined

    def inner():    # the inner function is defined within the outer function
        inner_var = 'World'  # a nested local variable inner_var is defined
        print(outer_var, inner_var)  # prints the outer_var and inner_var

    inner()  # the inner function is called explicitly

outer()  # the outer function is called

# The code will print "Hello World" because:
# The outer function defines a variable outer_var and the inner function can
# access outer_var because Python's scope rules allow nested functions to
# access variables in their enclosing function's scope.
# The inner function is defined within the outer function and is called
# explicitly inside the outer function. This triggers the print statement
# within the inner function, displaying the values of outer_var and
# inner_var variables.
# The outer function calls the inner_function, resulting in the output
# "Hello World".
