# What do you think the following code will output?
import math
nan_value = float("nan")

print(nan_value == float("nan"))  # False
print(math.isnan(nan_value))      # True
