# Which of the following values can't be used as a key in a 'dict' object, and why?
# Dictionary keys must be immutable and hashable.
# 'list', 'dictionaries', and 'sets' are all mutable and can not be used as keys

'cat'                             # string - immutable
(3, 1, 4, 1, 5, 9, 2)             # tuple - immutable
['a', 'b']                        # list - mutable  >>>>>>> can not be a key
{'a': 1, 'b': 2}                  # dictionary - mutable >> can not be a key
range(5)                          # range - immutable
{1, 4, 9, 16, 25}                 # set - mutable >>>>>>>>> can not be a key
3                                 # integer - immutable
0.0                               # float - immutable
frozenset({1, 4, 9, 16, 25})      # frozenset - immutable

