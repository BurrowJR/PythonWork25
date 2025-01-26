my_list = [
    1, 3, 6, 11, 4, 2, 4, 9, 17, 16, 0,
]

new_list = []
for element in my_list:
    if element % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')
print(new_list)

print()

result = ['even' if number % 2 == 0 else 'odd' 
          for number in my_list]
print(result)

print()

def even_odd(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ even_odd(number)
          for number in my_list ]
print(result)