def penultimate(string):
    return string.split()[-2]

print(penultimate("last word"))

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")