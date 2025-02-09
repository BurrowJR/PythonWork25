# Rewrite your code form the previous exercise to use a ternary expression.

import random
random_number = random.randint(0, 1)

print(random_number)

# if random_number == True:     # do not have to put == True here
#     print('Yes!')
# else:
#     print('No')

print('Yes!' if random_number else 'No')