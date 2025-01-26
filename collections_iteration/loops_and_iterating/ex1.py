# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)
    counter =+ 1   # without this line of code the counter is never incremented and the counter is always truthy and creates an infinite loop. 
