# Determine whether the following dictionary of people and their
# age contains an entry for 'Spot':

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('Spot' in ages)

def search_key(name):
    for key, value in ages.items():
        if key == name:
            print(f"{name} is {value} years old.")
            break
    else:
            print(f"{name} is not found")

search_key('Spot')
search_key('Grandpa')