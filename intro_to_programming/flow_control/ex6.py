def ex6(my_string):
    if len(my_string) > 10:
        return my_string.upper()
    else:
        return my_string

print(ex6('hello world'))
print(ex6('goodbye'))
