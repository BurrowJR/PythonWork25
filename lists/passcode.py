passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

def list_to_string(lst, delimiter="-"):
    return delimiter.join(lst)

new_code = list_to_string(passcode)
print(new_code)

# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs
print()

print('-'.join(passcode))

print()

joined_passcode = ''

for i in range(len(passcode)):
    if i > 0:
        joined_passcode += '-'
    
    joined_passcode += passcode[i]

print(joined_passcode)
