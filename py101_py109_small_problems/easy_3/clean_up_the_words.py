def clean_up(string):
    cleaned_up_string = []
    previous_space = False
    for char in string:
        if char.isalpha():
            cleaned_up_string.append(char)
            previous_space = False
        elif not previous_space:
            cleaned_up_string.append(" ")
            previous_space = True

    return ''.join(cleaned_up_string)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True