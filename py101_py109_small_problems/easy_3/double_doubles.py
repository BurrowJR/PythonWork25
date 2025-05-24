def double_number(number):
    number_to_string = str(number)
    middle = len(number_to_string) // 2
    return len(number_to_string) % 2 == 0 and number_to_string[:middle] == number_to_string[middle:]

def twice(number):
    if double_number(number):
        return number
    else:
        return number * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True