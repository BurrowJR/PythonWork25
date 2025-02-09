# Write an 'if' statement that prints 'Yes!' if 'random_number' is '1', and 'No' if random_number is '0'.

import random
random_number = random.randint(0, 1)
print(random_number)
if random_number == True:     # do not have to put == True here
    print('Yes!')
else:
    print('No')