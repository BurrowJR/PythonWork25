# What will the following two lines of code output?
print(0.3 + 0.6)         # 0.89999
print(0.3 + 0.6 == 0.9)  # False

# This happens because of rounding issues with the program.
# How to fix
import math
print(math.isclose(0.3 + 0.6, 0.9))    # True

# Floating point numbers for all numeric operations