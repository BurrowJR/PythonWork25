def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# If my_list is truthy (my_list contains elements) print('Not Empty')
# If my_list is falsy (my_list is empty) print ('Empty')
# The call of is_list_empty on line 7 will print 'Empty' because empty list are falsy. 
# The if block is skipped and the else block is ran.

is_list_empty([1, 2, 3])
is_list_empty([0])  # a list with the element 0 is truthy
is_list_empty(0)    # the integer 0 is falsy