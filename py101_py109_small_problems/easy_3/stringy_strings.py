def stringy(number):
    code = []
    for i in range(number):
        if i % 2 == 0:
             code.append("1")
        else:
            code.append("0")
    return ''.join(code)

print(stringy(6))

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True