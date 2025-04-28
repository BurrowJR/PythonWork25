# What will the following code print and why?
num = 5  # global variable num initialized to 5

def my_func():   # function my_func defined with no parameters
    num = 10     # local variable num initialized to 10

my_func()        # call my_func
print(num)       # print the global variable num which is 5
# This code will print 5 because the global variable num is not modified inside
# the my_func function. The local variable num inside my_func shadows the
# global variable num, but it does not affect its value. When my_func is
# called, it creates a new local variable num with the value 10, but this
# does not change the value of the global variable num. Therefore, when
# we print num after calling my_func, it still has the value 5.