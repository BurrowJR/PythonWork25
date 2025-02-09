# What is the official place to find Python documentation?
print('At the docs.python.org website.')

# Reviewing the documentation; some code I found interesting.


# Fibonacci sequence

a, b = 0, 1    # a = 0  b = 1
while a < 10:
    print(a, end=',') # print(a, b)
    a, b = b, a + b   # a = b(1) , b = 0 + 1 (1)
                      # a = 1 , b = 1 + 1 (2)

print(a)

print(f'{a} = a : {b} = b')

word = 'Python'
print(word[0])
my_word = word[2] + word[4]
print(my_word)

users = {'Hans': 'active', 'Elenonore': 'inactive', 'Betty': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
print()

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print()

def ask_ok(prompt, retries= 4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Ok to overwrite the file?', 2, 'Come on, only yes or no!')
