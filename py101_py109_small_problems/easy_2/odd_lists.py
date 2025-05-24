def oddities(lst):
    return lst[ : :2]

print(oddities([2, 3, 4, 5, 6]))
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

def oddities_2(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 != 0:
            result.append(lst[i])
    return result

print(oddities_2([2, 3, 4, 5, 6, 7]))
print(oddities_2(["abc", "def", "ghi", "jkl"]))
print(oddities_2([]))

def oddities_3(lst):
    result_2 = []
    for i, value in enumerate(lst):
        if i % 2 != 0:
            result_2.append(value)
    return result_2

print(oddities_3([2, 3, 4, 5, 6, 7]))
print(oddities_3(["abc", "def", "ghi", "jkl"]))
print(oddities_3([]))
