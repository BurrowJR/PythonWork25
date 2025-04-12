def floating_point():
    def get_number(prompt):
        return float(input(prompt))
    
    def perform_operations(a, b):
        operations = [
            ("+", lambda x, y: x + y),
            ("-", lambda x, y: x - y),
            ("*", lambda x, y: x * y),
            ("/", lambda x, y: x / y),
            ("//", lambda x, y: x // y),
            ("%", lambda x, y: x % y),
            ("**", lambda x, y: x**y),
        ]
        for op, func in operations:
            print(f"==> {a} {op} {b} = {func(a, b)}")
    
    first_number = get_number("==> Enter the first number:\n")
    second_number = get_number("==> Enter the second number:\n")

    perform_operations(first_number, second_number)

floating_point()