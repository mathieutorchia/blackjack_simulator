import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from blackjack_dev import *

results_global = []
results_session = []
p_strategy = 1
d_strategy = 1


player_cards = []
dealer_cards = []
dealer_sum = 0
player_sum = 0
result = ""
money = 0
# start the game by dealing 2 cards to the player and 1 card to the dealer
player_sum, dealer_sum, equal_cards, soft_hand = start_game(player_sum, dealer_sum, player_cards, dealer_cards)
player_first_cards = player_cards[0] + player_cards[1]
dealer_first_card = dealer_cards[0]

# dealer plays
# play the dealer first because it helps for the splitting logic
dealer_sum = dealer_strategy(dealer_first_card, dealer_cards, d_strategy)


print(f"player's cards: {player_cards}, sum of {player_sum}.")
print(f"dealer's cards: {dealer_cards}, sum of {dealer_sum}.")











# print(f"the result is {result}, and the money is {money}.")

