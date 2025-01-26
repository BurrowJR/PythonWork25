cats = ('Cocoa', 'Cheddar', 'Pudding', 'Butterscotch')

print('Butterscotch' in cats)   # True
print('Butter' in cats)         # False  must match all the elements in the
                                # string
print('Butter' in cats[3])      # True  is only looking at index 3 does not 
                                # have to be the whole string
print('cheddar' in cats)        # False  'c' is not the same as 'C'