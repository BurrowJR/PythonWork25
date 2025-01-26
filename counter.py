counter = 1
while counter <= 10:
    print(counter)
    counter += 1


'''
This code /iterates/ over the block for all integer values between 1 and 10, inclusive. Each time the block runs is called an /iteration/.

When Python encounters this while loop, it evaluates the conditional expression, 'counter <= 10'. Since 'counter's' initial value is 1, the expression is initially True, so Python executes the block. We print 'counter's' value inside the block, then increment it by 1.
Python then re-evaluates the conditional expression. This time, 'counter' is 2, which is still less than or equal to 10; thus, the block runs again. After 10 iterations, 'counter's' value becomes 11. Since the loop condition is no longer truthy, the program stops looping, It continues with the first expression or statement after the loop.
'''