# What will the following code do?
def my_func():    # the function my_func is defined with no parameters
    num = 10      # a local variable num is defined

my_func()         # the function my_func is called
print(num)        # an attempt to print the variable num is made
# The code will raise a NameError because:
# The variable num is defined within the local scope of the function my_func
# and is not accessible outside of that function. When the print statement
# tries to access num, it raises a NameError indicating that num is not
# defined in the global scope. 