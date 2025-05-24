def get_name():
    while True:
        try:
            name = input("What is your name?  ")
            if '!' in name:
                print(f"HELLO {name.upper()}! WHY ARE WE YELLING?")
                break
            elif not name.isalpha():
                print("Can I have your name please?")
            else:
                print(f"Hello, {name.capitalize()}.")
                break
        except ValueError:
            print("Error: Please enter your name.")

get_name()
