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
        return 'player'

    if player in winning_combinations[computer]:
        prompt('Computer wins!')
        return 'computer'

    prompt("It's a tie!")
    return 'tie'

def prompt(message):
    print(f'==> {message}')

print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
print()
while True:
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        prompt(
            f'Choose one: {', '.join(VALID_CHOICES)} or \nuse: {ABBREVIATIONS}'
            )
        choice = input().lower()

        if choice in CHOICE_MAP:
            choice = CHOICE_MAP[choice]
        elif choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            continue

        computer_choice = random.choice(VALID_CHOICES)
        result = display_winner(choice, computer_choice)

        if result == 'player':
            player_score += 1
        elif result == 'computer':
            computer_score += 1
        prompt(f"Score: You {player_score}, Computer {computer_score}")

    if player_score == 3:
        prompt("Congratulations! You won the game!")
    else:
        prompt("Sorry, the computer won the game.")

    while True:
        prompt("Do you want to play again? (y/n)")
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
    if answer.startswith('n'):
        prompt('Thanks for playing!')
        break