import random
import pandas as pd
import matplotlib.pyplot as plt

def getCard(person_cards):
    """takes the persons cards (list) as input, and adds 1 card to their list, and adds the sum.
    It will also change the value of an 11 to 1 if total > 21"""
    card = random.choice(cards)
    person_cards.append(card)

    total = 0
    length = len(person_cards)
    for i in range(0, length):
        total += person_cards[i]

    for i in range(0, length):
        if person_cards[i] == 11 and total > 21:
            person_cards[i] = 1
            total -= 10

    return total


def hasEleven(list):
    """Takes a list of cards as input, and return True if one of the cards is an eleven"""
    length = len(list)
    for i in range(0, length):
        if list[i] == 11:
            return True
    return False


def startGame(player_sum, dealer_sum):
    """this takes the player and dealer sums, and then adds a card to their arrays, and returns the new sums"""
    player_sum = getCard(player_cards)
    player_sum = getCard(player_cards)
    dealer_sum = getCard(dealer_cards)
    # print(f"Dealer shows a {dealer_cards} for a total of {dealer_sum}.")
    # print(f"Player shows a {player_cards} for a total of {player_sum}.")
    return player_sum, dealer_sum


# simple strategy:
# (1) if dealer has less than 7, hit until you get to 12
# (2) if dealer has 7 or more, hit until you get to 17

# Running the entire simulation
hands = 100
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
results = []
money = 0
for iteration in range(0, hands):

    # Storing the player/dealer cards for the game
    player_cards = []
    dealer_cards = []

    # Storing the sum of the cards
    player_sum = 0
    dealer_sum = 0

    # Storing a "W", "L" or "T"
    result = ""

    # Start of game
    player_sum, dealer_sum = startGame(player_sum, dealer_sum)
    player_first_cards = player_cards[0] + player_cards[1]
    dealer_first_card = dealer_cards[0]

    # Player Strategy
    if dealer_sum <= 6:
        while player_sum <= 11:
            player_sum = getCard(player_cards)
    else:
        while player_sum <= 16:
            player_sum = getCard(player_cards)

    # Dealer Strategy
    while dealer_sum <= 16:
        dealer_sum = getCard(dealer_cards)

    # Record Results
    if player_sum > 21:
        result = "L"
    elif dealer_sum > 21:
        result = "W"
    elif player_sum > dealer_sum:
        result = "W"
    elif player_sum < dealer_sum:
        result = "L"
    elif player_sum == dealer_sum:
        result = "T"

    if result == "W":
        money += 1
    elif result == "L":
        money -= 1

    # Appending some key factors from the game to the results list
    results.append([iteration, player_first_cards, dealer_first_card, result, money])

# Turning the results list into a dataframe
df = pd.DataFrame(results, columns=['iteration','player_first_cards', 'dealer_first_card', 'result', 'money'])
print(df)

# Counting the number of W, L, and T's
value_counts = df['result'].value_counts()
print(value_counts)

# Counting the percentage of times that we win based on the dealer upcard
percentage_w_per_card = df.groupby('dealer_first_card')['result'].apply(lambda x: (x == 'W').mean() * 100)
print(percentage_w_per_card)

# Plotting your bankroll over time
plt.plot(df['iteration'], df['money'], marker = 'o', linestyle = '-')
plt.xlabel('Iteration')
plt.ylabel('Money')
plt.title('Plotting Money vs. Number of BlackJack Hands')
plt.show()



