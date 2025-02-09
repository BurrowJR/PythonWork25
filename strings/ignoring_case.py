name = 'Roger'
string = 'RoGeR'
print(f'{name} and {string} are equal:  {name == string}')
print()
print(f'{name} and {string} are equal: {name.lower() == string.lower()}')
string_2 = 'DAVE'
print(f'{name} and {string_2} are equal: {name.casefold() == string_2.casefold()}')
print()
german = "SS"
german_2 = "ß"

print(german.casefold() == german_2.casefold())
print(german.lower() == german_2.lower())
