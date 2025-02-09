print(" Is there a method to reverse a string, for example turning 'hello' into 'olleh'? ")
print()

text = "This is some text!"
print(reversed(text))
print(list(reversed(text)))
print(''.join(reversed(text)))

print('Could also use slicing, but this is not a method.')

print(text[::-1])