scores = [96, 47, 113, 89, 100, 102]

def greater_than_99(element):
    count = [element for element in scores if element >= 100]
    print(len(count))

greater_than_99(scores)

print()

count = 0

for score in scores:
    if score >= 100:
        count += 1

print(count)
        