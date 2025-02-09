text = 'Captain Ruby'
print(text.replace('Ruby', 'Python' )) # non-mutating
print(f'{text}       original string')
text_2 = text.replace('Ruby', 'Python') # creates a new string
print(f'{text_2}     creating a new string with str.replace()')
print()

first_8 = 'Captain Ruby'[:8]
print(f'{first_8}           just first 8 char')
new_text = first_8 + 'Python'
print(f'{new_text}     concatenate Python')
print()

all_words = text.split(' ')
print(f'{all_words}    using str.split() ')
first_word = all_words[0]
print(f'{first_word}                extracting the first word')
new_str = first_word + ' Python'
print(f'{new_str}         concatenating Python to a new string')