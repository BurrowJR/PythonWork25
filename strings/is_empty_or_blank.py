def is_empty_or_blank(string):
    return string.strip() == ""

print(is_empty_or_blank('mars'))
print(is_empty_or_blank('   '))
print(is_empty_or_blank(''))

def is_empty_or_blank(string):
    return not string.strip(' ')

print(is_empty_or_blank('  '))