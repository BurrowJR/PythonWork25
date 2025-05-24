# What is the output of the following code?

answer = 42    # global scope

def mess_with_it(some_number):
    return some_number + 8        # 42 + 8

new_answer = mess_with_it(answer)  # local scope no effect on answer
print(new_answer)     # outputs 50
print(answer - 8)   # global answer 42 - 8 = 34 output is 34