import random
weather = ['sunny', 'rainy', 'windy', 'snowy', 'cloudy', 'stormy', 'foggy', 'hail', 'freezing', 'tornado', 'all other']
current_weather = random.choice(weather)
print(current_weather)

match current_weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case 'windy':
        print('Hang on to your hat!')
    case 'snowy':
        print("Let's go sledding!")
    case 'cloudy':
        print('Grab a jacket.')
    case 'stormy':    
        print('Grab a rain coat!')
    case 'foggy':
        print('Grab a reflective vest.')
    case 'hail':
        print("Let's stay inside!")
    case 'freezing':
        print('Dress in layers, lots of layers!')
    case 'tornado':
        print('Run for the storm shelter!')
    case _:
        print("Think I'll stay home and code:)")