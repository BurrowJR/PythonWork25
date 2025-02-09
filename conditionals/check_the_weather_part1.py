import random
weather = ['sunny', 'rainy', 'windy', 'all other']
weather_selection = random.choice(weather)
print(weather_selection)

if weather_selection == 'sunny':
    print("It's a beautiful day!")
elif weather_selection == 'rainy':
    print('Grab your umbrella.')
elif weather_selection == 'windy':
    print('Hang on to your hat!')
else:
    print("Let's stay inside.")

