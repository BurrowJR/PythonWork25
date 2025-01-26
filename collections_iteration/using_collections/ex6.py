# What will the following code print?

print('abc-def'.isalpha())     # false -
print('abc_def'.isalpha())     # false _
print('abc def'.isalpha())     # false has a whitespace
print('abc def'.isalpha() and  # false has a whitespace
      'abc def'.isspace())     #       has letters
print('abc def'.isalpha() or   # false has a whitespace
      'abc def'.isspace())     #       has letters
print('abcdef'.isalpha())      # true
print('31415'.isdigit())       # true
print('-31415'.isdigit())      # false -
print('31_415'.isdigit())      # false _
print('3.1415'.isdigit())      # false .
print(''.isspace())            # false empty string