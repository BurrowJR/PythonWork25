value = int(input('Give me a positive number!  '))
#value = 20

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 nor 6')

# same as if/else

#value = 7

if value == 7:
    print('value is 7')
elif value == 8:
    print('value is 8')
else:
    print('value is neither 7 or 8')

    