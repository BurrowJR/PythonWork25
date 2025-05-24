# Given the following similar sets of code, what will each code snippet print?

print("A")
def mess_with_vars(one, two, three):
    one = two 
    two = three 
    three = one 

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")    # ["one"]
print(f"two is: {two}")    # ["two"]
print(f"three is: {three}")# ["three"]

print("B")
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")      # ["one"]
print(f"two is: {two}")      # ["two"]
print(f"three is: {three}")  # ["three"]

print("C")
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")      # ["one"]
print(f"two is: {two}")      # ["two"]
print(f"three is: {three}")  # ["three"]