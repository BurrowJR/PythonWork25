print(' Use the Python documentation for the str class to determine which\n method can be used to right justify a str object. ')
print()

print(' str.rjust(width[, fillchar] ')
print('The original string is returned if width is less than or equal to len(s).')
print()

text = 'This is some text'
print(len(text))
right_justify = text.rjust(18, '-')
print(right_justify)

print('This will return original string'.rjust(18, '-'))
print('This works properly'.rjust(25, '-'))

