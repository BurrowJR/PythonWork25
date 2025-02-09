def starts_with(string, prefix):
    return string.startswith(prefix)

print(starts_with('launch', 'la'))
print(starts_with('school', 'sah'))
print(starts_with('school', 'sch'))

print()

def starts_with(string, prefix):
    if len(prefix) > len(string):
        return False
    for i in range(len(prefix)): 
        if string[i] != prefix[i]:
            return False
    return True

print(starts_with('launch', 'la'))
print(starts_with('school', 'sah'))
print(starts_with('school', 'sch'))