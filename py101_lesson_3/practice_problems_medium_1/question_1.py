# For this practice problem, write a program that outputs
# The Flintstones Rock! 10 times, with each line prefixed by one
# more hyphen than the line above it. The output should start out
# like this:


text = "The Flinstones Rock!"

hyphen = ""
for _ in range(1, 11):
    hyphen += "-"
    print(hyphen + text)

for i in range(11, 21):
    print(">" * i + text)

arrow = ["<"] * 20
for i in range(20, 11, -1):
    print("".join(arrow[:i]) + text)

for i in range(11, 0, -1):
    print("-" * i + text)