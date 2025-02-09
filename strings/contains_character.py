char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
character = 'x'
print(character in char_sequence)

print()

find_characters = []
index = char_sequence.find(character)
while index != -1:
    find_characters.append(index)
    index = char_sequence.find(character, index + 1)

print(f'{character} is at index {find_characters}')
