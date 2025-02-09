b = [1, 2, 3]

def my_function():
    b[0] = 10  # index reassignment mutates the list
    print(b)   # changed for verification

print(b)       # [1, 2, 3]
my_function()  # [10, 2, 3]
print(b)       # [10, 2, 3]  this only changes if my_function() is called first