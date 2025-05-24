# Write a function that takes one integer argument and returns True
# when the number's absolute value is odd, False otherwise.

# The absolute value of a number is its distance from zero on the number lie,
# regardless of direction. It is always non-negative.
# if x is positive or zero, then |x| = x
# if x is negative, then |x| = -x (which makes it positive)


def  absolute_value(number):
    return abs(number) % 2 != 0    # True if absolute value is odd

print(absolute_value(3))
print(absolute_value(8))
print(absolute_value(-5))
print(absolute_value(0))
