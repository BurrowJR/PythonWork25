# Modify the following code so the loop continues iterating until the user inputs 'yes'.

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':   # or answer == 'y' or answer == 'ye':
        break
    elif answer != 'yes' or answer != 'no':
        print('Invalid answer. Please answer "yes" or "no".') 