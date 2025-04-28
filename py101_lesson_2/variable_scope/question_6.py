# What wil the following code print and why?
def my_func():    # a function my_func is defined with no parameters
    x = 15        # a local variable x is defined

    def inner_func1():  # inner_func1 is defined within my_func
        x = 25          # a local variable x is defined within inner_func1
        print("Inner 1:", x) # prints the local x of inner_func1 25
    
    def inner_func2():  # inner_func2 is defined within my_func
        print("Inner 2:", x) # prints the local x of my_func 15
    
    inner_func1()  # inner_func1 is explicitly called
    inner_func2()  # inner_func2 is explicitly called

my_func()   # my_func function is called

# The code will print:
# Inner 1: 25
# Inner 2: 15
# The first print statement in inner_func1 prints the local variable x of
# inner_func1, which is 25. The second print statement in inner_func2
# prints the local variable x of my_func, which is 15. The inner functions
# can access the variables in their enclosing function's scope, but they
# have their own local variables that can shadow the outer variables.