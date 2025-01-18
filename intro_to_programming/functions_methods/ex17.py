def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

'''
Which of the identifiers in the following program are function names?
which are method names? Which are built-in functions?
function name:
say()

method name:
.upper()
.lower()

built-in function:
print()
input()
max()

'''