def first(first_element):
    if len(first_element) > 0:    # do not have to use > 0
        return first_element[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))
print(first(['One']))
print(first([]))

print()

def first(lst):
    if lst:
        return lst[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))
print(first(['One']))
print(first([]))
