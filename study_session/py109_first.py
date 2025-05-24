text = 'Hello! I am Eloise'  # strings are immutable

def swap(s):
    for char in s:
        s.replace(char, char.upper()) # does not change original string
    return s   # this returns original sting

print(swap(text)) # function invocation prints original text
print(text)
print()
text = 'Hello! I am Eloise'

def swap(s):
    for char in s:
        text = s.replace(char, char.upper()) # str.replace iterates through the string
        # changing the last char to an upper E
        text = s.replace('am', 'am'.upper())  # Hello! I AM Eloise
    return text

print(swap(text))
print(text)
print()
greeting = "Hello"  # global variable

def greet():
    greeting = "Hi"  # local variable

greet()              # function invocation  None
print(greeting)      # Hello
print()

greeting = "Hello"

def greet():
    global greeting  # without the global keyword greeting is undefined and 
    # will return an UnboundLocal Error
    greeting += " world"
    print(greeting)

greet() 
print(greeting) # global keyword reassigns this greeting to Hello world.

print()

players = [
  {'name': "Joe", 'age': 25},
  {'name': "Andy", 'age': 31},
  {'name': "Ralph", 'age': 18},
  {'name': "Mark", 'age': 28},
]  # a list of dictionaries
   # each name is an element in the list

def older_than_age(players_list, age_threshold):
    for player in players_list:
        if player['age'] > age_threshold:  # if  player(key, value) > targeted_age
            return True
    
    return False

print(older_than_age(players, 30)) # True
print(older_than_age(players, 31)) # False
# This code is asking if any of the players in the list are greater than the
# argument age.