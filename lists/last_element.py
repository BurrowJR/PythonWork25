def last(lst):
    if lst:
        return lst[-1]
    else:
        None

print(last(['Earth', 'Moon', 'Mars']))
print(last(['Earth']))
print(last([]))