words = ['scooby', 'do', 'on', 'channel', 'two']

for word in words:
    print(word)

print(' '.join(words))

for word in words[:]:
    print(word)
    words.remove(word)
print(words)

print()
words = ['scooby', 'do', 'on', 'channel', 'two']

while words:
    print(words[0])
    words.pop(0)
print(words)
