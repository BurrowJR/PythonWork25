def crunch(string):
    daily_double = []
    prev_char = ''

    for char in string:
        if char != prev_char:
            daily_double.append(char)
            prev_char = char

    return ''.join(daily_double)

print(crunch('ddaaiillyy ddoouubbllee'))

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
