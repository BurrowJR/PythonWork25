def compare_by_length(string_1, string_2):
    if len(string_1) < len(string_2):
        return -1
    elif len(string_1) > len(string_2):
        return 1
    else:
        return 0

print(compare_by_length('patience', 'perseverance'))
print(compare_by_length('strength', 'dignity'))
print(compare_by_length('humor', 'grace'))