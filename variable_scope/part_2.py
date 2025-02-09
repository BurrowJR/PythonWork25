x = 10

def my_function():
    # x =20       must assign a value to 'x' inside function
    global x     # or use the global function
    x = x + 5
    print(x)

my_function()   # UnboundLocal Error: cannot access local variable 'x' where it is not associated with a value.

if x:
    x = x * 5
    print(x)
