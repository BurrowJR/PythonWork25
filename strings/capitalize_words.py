words = 'launch school tech & talk'
capitalized_words = words.title()
print(capitalized_words)

print()

def capitalize_words(string):
    words = string.split(' ')
    print(words)
    capitalized_words = []

    for word in words:
        capitalized_words.append(word.capitalize())
        print(capitalized_words)
    return ' '.join(capitalized_words)

string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)

print()

def capitalized_words(string):
    return(string.title())

string = 'hello world goodby'
result = capitalized_words(string)
print(result)
