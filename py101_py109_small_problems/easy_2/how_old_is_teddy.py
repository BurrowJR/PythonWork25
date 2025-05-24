from random import randint

def teddy_age():
    name = input("Give me a name? " ).strip() or "Teddy"
    print(f"{name} is {randint(20, 100)} years old!")

teddy_age()
