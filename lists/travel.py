destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(destination, lst):
    for element in lst:
        if element == destination:
            return True
    return False

print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))

print()

def contains(element, lst):
    index = 0
    while index < len(lst):
        if lst[index] == element:
            return "Found it!"
                
        index += 1
    return "Nope, not here!"

print(contains('Amarillo', destinations))
print(contains('Aruba', destinations))

print()

def contains(element, lst):
    return element in lst

print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))
print(contains('Amarillo', destinations))
print(contains('Aruba', destinations))