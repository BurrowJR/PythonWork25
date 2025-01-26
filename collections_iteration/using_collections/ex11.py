print('johnson' in 'Joe Johnson')           # False j != J
print('sen' not in 'Joe Johnson')           # True
print('Joe J' in 'Joe Johnson')             # True
print(5 in range(5))                        # False  range(5) = 0, 1, 2, 3, 4
print(5 in range(6))                        # True range(6) = 0, 1, 2, 3, 4, 5
print(5 not in range(5, 10))                # False range(5, 10) = 5, 6, 7, 8, 9
print(0 in range(10, 0, -1))                # False range(10, 0, -1) = 
                                              # 10, 9,  8, 7, 6, 5, 4, 3, 2, 1
print(4 in {6, 5, 4, 3, 2, 1})              # True
print({1, 2, 3} in {1, 2, 3})               # False because sets can not 
                                              # contain another set
print({3, 2} in {1, frozenset({2, 3})})     # True