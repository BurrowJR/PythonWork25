# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)   # {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}
# Since sets are unordered collections set2 could print in any order, but will contain all these elements.
