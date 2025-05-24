# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()  #  creates lazy sequence
my_list2[0]['first'] = 42
# my_list2 index 0 (first element) = {"first": 42}
print(my_list1)  # nested copies are NOT copied
# [{"first": 42}, {"second": "value2"}, 3, 4, 5]