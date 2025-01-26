# In your own words, explain the difference between these two expressions.

my_object1 = 'hello world'
my_object2 = my_object1

my_object1 == my_object2  #  == compares the 2 objects to see if they have the
                          # same value or elements -- value equality
my_object1 is my_object2  # is checks to see if the 2 objects reference the
                          # same place in memory  -- object equality

print(my_object1 == my_object2)
print(my_object1 is my_object2)
print(id(my_object1))
print(id(my_object2))
print()
my_object2 = 'good bye world'

print(my_object1 == my_object2)
print(my_object1 is my_object2)
print(id(my_object1))
print(id(my_object2))
print()