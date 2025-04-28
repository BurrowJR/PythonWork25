# What will the following code print and why?
num = 5    # global variable initialized to 5

def my_func():   # define my_func that takes no parameters
    print(num)   # print the value of the global variable num

my_func()        # call my_func

# The code will print 5.
# The function my_func accesses the global variable num,
# which is initialized to 5.
# Since there is no local variable num defined within my_func,
# it uses the global variable num.