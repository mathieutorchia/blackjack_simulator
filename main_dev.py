import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from blackjack_dev import (get_card,start_game, split, dealer_strategy, has_eleven, clear_terminal,
                           strategy_split, strategy_normal, data_money)

def run_blackjack_simulation():

    example_player = [[]]
    example_dealer = [[]]
    total_hands = 0
    hand_sums = [0]
    hand_sums_start = [0]
    data_split = False
    data_result = []
    data_result_reason = []
    data_hand_result = []
    last_action = [""]


    # Start the game and ask for a decision
    dealer_sum = start_game(example_player, example_dealer)
    data_dealer_first = dealer_sum

    # decision = input("Would you like to split? (yes or no) ")
    decision = strategy_split(example_player,data_dealer_first,0)



    # Splitting all hands until we're done
    if decision == "once":
        data_split = True
        hand_sums.append(0)
        hand_sums_start.append(0)
        last_action.append("")
        split(example_player,0)
        total_hands = 2
    if decision == "no":
        total_hands = 1
    if decision == "yes":
        data_split = True
        hand_sums.append(0)
        hand_sums_start.append(0)
        last_action.append("")
        split(example_player, 0)
        while total_hands < len(example_player):
            # print(f"Here are your hands: {example_player}")
            decision = strategy_split(example_player,data_dealer_first,total_hands)
            if decision == "yes":
                hand_sums.append(0)
                hand_sums_start.append(0)
                last_action.append("")
                split(example_player, total_hands)
            if decision == "no":
                total_hands += 1

    # putting the sum of all hands in the hand_sums variable
    for hand in range(0, total_hands):
        hand_sums[hand] = example_player[hand][0] + example_player[hand][1]
        hand_sums_start[hand] = example_player[hand][0] + example_player[hand][1]

    # playing the game
    for hand in range(0,total_hands):
        decision = strategy_normal(example_player,hand_sums,data_dealer_first,hand)
        if decision == "double":
            hand_sums[hand] = get_card(example_player, hand)
            last_action[hand] = "double"
        if decision == "stand":
            last_action[hand] = "stand"
        while decision == "hit":
            hand_sums[hand] = get_card(example_player, hand)
            last_action[hand] = "hit"
            if hand_sums[hand] > 21:
                # print("You busted")
                decision = "busted"
            else:
                decision = strategy_normal(example_player,hand_sums,data_dealer_first,hand)
                last_action[hand] = decision

    # dealer plays
    dealer_sum = dealer_strategy(dealer_sum,example_dealer,1)


    # communicate the results
    for hand in range(0,total_hands):
        # print("")
        # print(f"HAND NUMBER {hand+1}")
        if hand_sums[hand] > 21:
            # print(f"You lost")
            # print("You busted")
            data_result.append("L")
            data_result_reason.append("Player bust")
        elif dealer_sum > 21:
            # print(f"You won.")
            # print("Dealer busted.")
            data_result.append("W")
            data_result_reason.append("Dealer bust")
        elif hand_sums[hand] > dealer_sum:
            # print("You won.")
            # print(f"Your {hand_sums[hand]} beat the dealer's {dealer_sum}.")
            data_result.append("W")
            data_result_reason.append("Player closer to 21")
        elif hand_sums[hand] < dealer_sum:
            # print("You lost.")
            # print(f"Your {hand_sums[hand]} was beat by the dealer's {dealer_sum}.")
            data_result.append("L")
            data_result_reason.append("Dealer closer to 21")
        elif hand_sums[hand] == dealer_sum:
            # print("You tied")
            # print(f"Your {hand_sums[hand]} was equal to the dealer's {dealer_sum}.")
            data_result.append("T")
            data_result_reason.append("Tie")
        # print("")

    for hand in range(0,total_hands):
        data_hand_result.append([hand, hand_sums_start[hand], hand_sums[hand], data_dealer_first, data_split ,dealer_sum,
                                 data_result[hand], last_action[hand], data_result_reason[hand]])

    df = pd.DataFrame(data_hand_result,columns=['hand', 'hand_sum_start', 'hand_sum', 'dealer_first', 'data_split',
                                                'dealer', 'result', 'last_action', 'reason'])

    df['money'] = df.apply(data_money, axis=1)

    return df


if __name__ == "__main__":
    df = run_blackjack_simulation()
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', None)  # Adjust the width to prevent line breaks
    print(df)




    # print(f"Your cards are: {example_player}.")
    # print(f"Your sums are: {hand_sums}.")
    # print(f"The dealer had: {example_dealer}, which is a total of {dealer_sum}.")
    # print(f"The player split: {data_split}.")
    # print(f"The final result: {data_result}")

