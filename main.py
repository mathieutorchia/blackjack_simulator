import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from blackjack import get_card, has_eleven, start_game, player_strategy, dealer_strategy, record_result

hands = 1000
results_global = []
sessions = 1000
line_chart = True
histogram_chart = True
smooth_chart = True
p_strategy = 2
d_strategy = 1

for session in range(1,sessions+1):
    money_session = 0
    results_session = []

    for hand in range(1, hands+1):
        money_hand = 0
        player_cards = []
        dealer_cards = []
        dealer_sum = 0
        player_sum = 0
        result = ""
        # start the game by dealing 2 cards to the player and 1 card to the dealer
        player_sum, dealer_sum, equal_cards, soft_hand = start_game(player_sum,dealer_sum,player_cards,dealer_cards)
        player_first_cards = player_cards[0] + player_cards[1]
        dealer_first_card = dealer_cards[0]

        # play the game
        player_sum = player_strategy(player_sum, dealer_sum, player_cards,p_strategy)

        # dealer plays
        dealer_sum = dealer_strategy(dealer_sum,dealer_cards,d_strategy)

        # record results, and update money
        result, money_session, money_hand = record_result(player_sum, dealer_sum, money_session)

        results_session.append([session, hand, player_first_cards, dealer_first_card, result, money_session, money_hand])

    results_global.extend(results_session)


df = pd.DataFrame(results_global,columns=['session', 'hand', 'player_first_cards', 'dealer_first_card', 'result', 'money_session', 'money_hand'])
df_simplified = df.groupby('session')['money_hand'].mean().reset_index()


# Line Graph Chart
if line_chart:
    session_data = [group[1][['hand', 'money_session']] for group in df.groupby('session')]
    for session_data in session_data:
        plt.plot(session_data['hand'], session_data['money_session'])
    plt.style.use('ggplot')
    plt.xlabel('Number of Hands')
    plt.ylabel('Total Profit ($)')
    plt.title(f'Total Profit after {hands} hands, for {session} sessions.')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Histogram Chart
if histogram_chart:
    plt.hist(df_simplified['money_hand'], edgecolor = "skyblue", cumulative=False, alpha = 0.7)
    plt.style.use('ggplot')
    plt.xlabel("Average Profit per trip ($)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of profits over {hands} hands, across {session} sessions")
    plt.axvline(df_simplified['money_hand'].mean(), color = "red", linestyle="--", linewidth=2, label="Mean Profit")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Smooth Histogram Chart
if smooth_chart:
    sns.kdeplot(df_simplified['money_hand'], fill=True, color="skyblue")
    plt.style.use('ggplot')
    plt.xlabel("Average Profit per trip ($)")
    plt.ylabel("Density")
    plt.title(f"Distribution of profits over {hands} hands, across {session} sessions")
    plt.axvline(df_simplified['money_hand'].mean(), color="red", linestyle="--", linewidth=2, label="Mean Profit")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()











# print(f"player's cards: {player_cards}, sum of {player_sum}.")
# print(f"dealer's cards: {dealer_cards}, sum of {dealer_sum}.")
# print(f"the result is {result}, and the money is {money}.")
print(df)
print(df_simplified)