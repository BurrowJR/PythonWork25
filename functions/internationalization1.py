def greet(language_code):
   greetings = {
     'en': 'Hi!',
     'fr': 'Salut!',
     'pt': 'Olá!',
     'de': 'Hallo!',
     'sv': 'Hej!',
     'af': 'Haai!',
   } 
   return greetings.get(language_code, 'Hello!')

print(greet('en'))
print(greet('fr'))
print(greet('pt'))
print(greet('de'))
print(greet('sv'))
print(greet('af'))
print(greet('my'))