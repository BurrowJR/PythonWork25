def triangel(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)

triangel(10)

def centered_triangel(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n -1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

centered_triangel(10)