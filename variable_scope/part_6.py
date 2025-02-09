a = 1

def my_function():
   # global a   Would reassign the value of 'a' to 2 on line 8
   a = 2

my_function()  # returns None
print(a)       # prints 1
