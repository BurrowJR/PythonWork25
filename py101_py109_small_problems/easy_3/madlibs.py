print("Welcome to Madlib!")

def validate_word(word):
    try:
        word = word.strip()
        if not word:
            raise ValueError("Input cannot be empty!")
        return word
    except ValueError:
        print(f"Error: Try again.")
        return None

def get_valid_input(prompt):
    while True:
        word = input(">>>" + prompt).strip()
        valid_word = validate_word(word)
        if valid_word:
            return valid_word

def enter_words():
    noun = get_valid_input("Please enter a noun:  ")
    verb = get_valid_input("Please enter a verb:  ")
    adjective = get_valid_input("Please enter an adjective:  ")
    place = get_valid_input("Please enter an place:  ")
    plural_noun_1 = get_valid_input("Please enter an plural noun:  ")
    plural_noun_2 = get_valid_input("Please enter another plural noun:  ")
    plural_noun_3 = get_valid_input("Please enter one last plural noun:  ")
    an_object = get_valid_input("Please enter an object:  ")
    name_person = get_valid_input("Please enter the name of a person:  ")
    name_place = get_valid_input("Please enter the name of a place:  ")
    creature = get_valid_input("Please enter a type of creature:  ")
    title = get_valid_input("Please enter a title (pirate, captain, etc.):  ")

    print()
    story = f"""
    Ahoy, matey! Ye be settin' sail on a(n) {adjective} voyage across the
    {place.title()} in search of the legendary {noun.title()}.
    With a {adjective} crew and a trusty {an_object}, ye braved {plural_noun_1}
    and {plural_noun_2} to reach the island of {name_place.title()}.

    'Arrr! cried Captain {name_person.title()}. 'We must {verb} through the
    {adjective} jungle to find the treasure!' But beware--the path was littered
    with {plural_noun_3} and guarded by a fearsome {creature}.
    
    With a mighty {verb}, ye uncovered the treasure chest and claim yer prize,
    the sneaky {creature} tried to {verb} it away!
    
    Thinking fast, ye {verb} and saved the treasure. Now ye be the richest
    {title.title()} in all the {place.title()}!
    """
    print(story)

enter_words()