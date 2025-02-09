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

def extract_language(locale):
    parts = locale.split('_')
    language_code = parts[0]
    return language_code

def extract_region(locale):
    parts = locale.split('_')    # 'en', 'US.UTF-8' 
    language_region = parts[1].split('.')[0]
    return language_region

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case('en', 'US'):
            return 'Hey!'
        case('en', 'GB'):
            return 'Hello!'
        case('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('fr_FR.UTF-8'))
print(local_greet('fr_CA.UTF-8'))
print(local_greet('fr_MA.UTF-8'))
