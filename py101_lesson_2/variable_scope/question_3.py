# What will the following code print and why?
num = 5           # the global variable num is initialized to 5

def my_func():    # the function my_func is defined with no parameters
    global num    # the global keyword is used to refer to the
                  # global variable num
    num = 10      # the global variable num is reassigned to 10

my_func()         # the function my_func is called
print(num)        # the global variable num is printed

# The code will print 10 because the global variable num is reassigned
# to 10 inside the function my_func. The global keyword allows
# the function to modify the global variable num instead of creating
# a local variable with the same name. When my_func is called,
# it changes the value of num to 10, and when print(num) is executed,
# it prints the updated value of num, which is now 10.