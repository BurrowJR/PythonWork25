def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)

    increment_counter()
    print(counter)

    increment_counter()
    print(counter)

    counter = 100
    increment_counter()
    print(counter)

all_actions()
