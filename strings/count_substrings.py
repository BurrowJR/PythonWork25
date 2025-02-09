def count_substrings(string, substring):
    count = 0
    start = 0

    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += len(substring)
    return count

print(count_substrings('lemon lemon lemon', 'lemon'))
print(count_substrings('laLAlaLA', 'la'))
print(count_substrings('launch', 'uno'))

print()

def count_substrings(string, substring):
    return string.count(substring)
