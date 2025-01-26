keep_going = True
while keep_going:
    # main loop code is here

    answer = input('Play again? (y/n) ')
    if answer == 'n':
        keep_going = False

# can use while True and break
while True:
    # main loop code is here
     
    answer = input('Play again? (y/n) ')
    if answer == 'n':
        break
print()

# Simultaneous Iteration
forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0
while index < len(forenames):
    if index >= len(surnames):
        break
    
    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1

print()

zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')
print()

multiples_of_6 = [number for number in range(20)
                  if number % 6 == 0]
print(multiples_of_6)

print()

even_squares = [number * number 
                for number in range(10)
                if number % 2 == 0 ]
print(even_squares)

print()

cats_colors = {
    'Tess': 'brown',
    'Leo': 'orange',
    'Fluffy': 'gray',
    'Ben': 'black',
    'Kat': 'orange',
}

names = [name.upper() for name in cats_colors]
print(names)

colors = [name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange']
print(colors)

name_color = [name.upper()
              for name in cats_colors
              if cats_colors[name] == 'orange'
              if name[0] == 'L']
print(name_color)

print()

squares = {f' {number}-squared': number * number
           for number in range(1, 6)}
print(squares)

print()

squares = {number * number for number in range(6, 11)}
print(squares)
