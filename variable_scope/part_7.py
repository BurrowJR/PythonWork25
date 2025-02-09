a = 1

def my_function():
    global a
    a = 2       # reassigns 'a' from line 1

my_function()   # returns None  Must call the function to change 'a'
print(a)        # prints 2      this would print 1 if function not called