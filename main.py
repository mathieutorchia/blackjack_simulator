import random
import pandas as pd
import matplotlib.pyplot as plt
from blackjack import get_card, has_eleven, start_game, player_strategy, dealer_strategy, record_result

hands = 1000
results_global = []
sessions = 1000
line_chart = False
histogram_chart = True

for session in range(1,sessions+1):
    money = 0
    results_session = []

    for hand in range (1, hands+1):
        player_cards = []
        dealer_cards = []
        dealer_sum = 0
        player_sum = 0
        result = ""
        # start the game by dealing 2 cards to the player and 1 card to the dealer
        player_sum, dealer_sum = start_game(player_sum,dealer_sum,player_cards,dealer_cards)
        player_first_cards = player_cards[0] + player_cards[1]
        dealer_first_card = dealer_cards[0]

        # play the game
        player_sum = player_strategy(player_sum, dealer_sum, player_cards,2)

        # dealer plays
        dealer_sum = dealer_strategy(dealer_sum,dealer_cards,1)

        # record results, and update money
        result, money = record_result(player_sum, dealer_sum, money)

        results_session.append([session, hand, player_first_cards, dealer_first_card, result, money])

    results_global.extend(results_session)


df = pd.DataFrame(results_global,columns=['session', 'hand', 'player_first_cards', 'dealer_first_card', 'result', 'money'])
df_simplified = df.groupby('session')['money'].mean().reset_index()


# Line Graph Chart
if line_chart:
    session_data = [group[1][['hand', 'money']] for group in df.groupby('session')]
    for session_data in session_data:
        plt.plot(session_data['hand'], session_data['money'])
    plt.xlabel('Hands')
    plt.ylabel('Money')
    plt.title(f'Money vs. Hands for {sessions} Sessions')
    plt.show()

# Histogram Chart
if histogram_chart:
    plt.hist(df_simplified['money'], edgecolor = "skyblue", cumulative=False, alpha = 0.7)
    plt.style.use('ggplot')
    plt.xlabel("Average Profit per trip ($)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of profits over {hands} hands, across {session} sessions")
    plt.axvline(df_simplified['money'].mean(), color = "red", linestyle="--", linewidth=2, label="Mean Profit")
    plt.legend()
    plt.grid(True, linestyle = '--', alpha = 0.5)
    plt.show()









# print(f"player's cards: {player_cards}, sum of {player_sum}.")
# print(f"dealer's cards: {dealer_cards}, sum of {dealer_sum}.")
# print(f"the result is {result}, and the money is {money}.")