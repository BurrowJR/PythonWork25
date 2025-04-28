# Player Wins:
    # scissors    cuts paper*
    # paper       covers rock<
    # rock        crushes lizard>
    # lizard      poisons spock$
    # spock       smashes scissors#
    # scissors    decapitates lizard*
    # lizard      eats paper$
    # paper       disproves spock<
    # spock       vaporizes rock#
    # rock        crushes scissors>

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
CHOICE_MAP = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'sk': 'spock'
}
ABBREVIATIONS = ', '.join([
    f"{key} ({value})"
    for key, value in CHOICE_MAP.items()
    ])

def display_winner(player, computer):
    prompt(f' You chose {player}, computer chose {computer}.')

    winning_combinations = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    if computer in winning_combinations[player]:
        prompt('You win!')
    elif player in winning_combinations[computer]:
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

def prompt(message):
    print(f'==> {message}')

print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
print()
while True:
    prompt(f'Choose one: {', '.join(VALID_CHOICES)} or \nuse: {ABBREVIATIONS}')
    choice = input().lower()

    if choice in CHOICE_MAP:
        choice = CHOICE_MAP[choice]
    elif choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        continue

    computer_choice = random.choice(VALID_CHOICES)
    display_winner(choice, computer_choice)

    while True:
        prompt("Do you want to play again? (y/n)")
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')

    if answer[0] == 'n':
        prompt('Thanks for playing!')
        break