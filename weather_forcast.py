import random

random_weather = ['sunny', 'rainy', 'windy', 'stormy', 'hailing']
select_weather = random.choice(random_weather)

match select_weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella!")
    case 'windy':
        print("Hang on to your hat!")
    case 'stormy':
        print("Grab a rain coat!")
    case 'hailing':
        print("Let's stay inside!")
    case _:
        print("Something went wrong!")