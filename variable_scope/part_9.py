a = 7  # immutable so does not change after line5

def my_function(b):
    b += 10
    print(b)     # added this line for verification

my_function(a)   # prints 17
print(a)         # prints 7