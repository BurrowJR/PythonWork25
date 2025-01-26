suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)
#print(deck)

'''
With nested 'for' loops, you start with the outer loop and assign the variable to the first element of its collection (suit and suits). You then process the inner loop in its entirety. Here, we match the first suit with every possible card rank, appending each card to the deck.

Once the inner loop finishes processing, control returns to the outer loop. Working with the second element of the outer loop's collection, it again iterates over the inner loop's collection. This continues until all members of the outer loop's collection have been processed. In our card deck example, the outer loop runs 4 times, while the inner loop runs 4 * 13 (52) times.
'''

for suit in suits:
    print(f'{suit}:')
    for card in deck:
        if suit in card:
            print(f'   {card}')
