import random
import pandas as pd
import matplotlib.pyplot as plt



def get_card(person_cards):
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


def has_eleven(list):
    """Takes a list of cards as input, and return True if one of the cards is an eleven"""
    length = len(list)
    for i in range(0, length):
        if list[i] == 11:
            return True
    return False

def start_game(player_sum, dealer_sum):
    """this takes the player and dealer sums, and then adds a card to their arrays, and returns the new sums"""
    player_sum = get_card(player_cards)
    player_sum = get_card(player_cards)
    dealer_sum = get_card(dealer_cards)
    # print(f"Dealer shows a {dealer_cards} for a total of {dealer_sum}.")
    # print(f"Player shows a {player_cards} for a total of {player_sum}.")
    return player_sum, dealer_sum


# Running the entire simulation
hands = 100
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
results_global = []
trips = 100

for trip in range(0, trips):
    money = 0
    results_trip = []
    for hand in range(0, hands):

        # Storing the player/dealer cards for the game
        player_cards = []
        dealer_cards = []

        # Storing the sum of the cards
        player_sum = 0
        dealer_sum = 0

        # Storing a "W", "L" or "T"
        result = ""

        # Start of game
        player_sum, dealer_sum = start_game(player_sum, dealer_sum)
        player_first_cards = player_cards[0] + player_cards[1]
        dealer_first_card = dealer_cards[0]

        # Player Strategy
        if dealer_sum <= 6:
            while player_sum <= 11:
                player_sum = get_card(player_cards)
        else:
            while player_sum <= 16:
                player_sum = get_card(player_cards)

        # Dealer Strategy
        while dealer_sum <= 16:
            dealer_sum = get_card(dealer_cards)

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
        results_trip.append([trip, hand, player_first_cards, dealer_first_card, result, money])

    results_global.extend(results_trip)

df = pd.DataFrame(results_global,columns=['trip', 'hand', 'player_first_cards', 'dealer_first_card', 'result', 'money'])
df_simplified = df.groupby('trip')['money'].mean().reset_index()



plt.hist(df_simplified['money'], edgecolor = "skyblue", cumulative=False, alpha = 0.7)
plt.style.use('ggplot')
plt.xlabel("Average Profit per trip ($)")
plt.ylabel("Frequency")
plt.title(f"Distribution of profits over {hands} hands, across {trips} trips")
plt.axvline(df_simplified['money'].mean(), color = "red", linestyle="--", linewidth=2, label="Mean Profit")
plt.legend()
plt.grid(True, linestyle = '--', alpha = 0.5)

plt.show()





# Split the DataFrame into separate trips
trips_data = [group[1][['hand', 'money']] for group in df.groupby('trip')]

# Plot each trip separately
for trip_data in trips_data:
    plt.plot(trip_data['hand'], trip_data['money'])

# Set labels and title
plt.xlabel('Hands')
plt.ylabel('Money')
plt.title(f'Money vs. Hands for {trips} Trips')

# Show plot
plt.show()













visualize_data(df_simplified, trips, hands)







# # Counting the number of W, L, and T's
# value_counts = df['result'].value_counts()
# print(value_counts)
#
# # Counting the percentage of times that we win based on the dealer upcard
# percentage_w_per_card = df.groupby('dealer_first_card')['result'].apply(lambda x: (x == 'W').mean() * 100)
# print(percentage_w_per_card)
#
# # Plotting your bankroll over time
# plt.plot(df['iteration'], df['money'], marker = 'o', linestyle = '-')
# plt.xlabel('Iteration')
# plt.ylabel('Money')
# plt.title('Plotting Money vs. Number of BlackJack Hands')
# plt.show()





