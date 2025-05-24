# def xor(x, y):
#     return bool(x) ^ bool(y)

def xor(x, y):
    return bool(x) != bool(y)

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)