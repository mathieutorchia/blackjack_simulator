import random
import os


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def get_card(person_cards, hand_number):
    """takes the persons cards (list) as input, and adds 1 card to their list"""
    card = random.choice(cards)
    person_cards[hand_number].append(card)

    total = 0
    length = len(person_cards[hand_number])
    for i in range(0, length):
        total += person_cards[hand_number][i]

    for i in range(0, length):
        if person_cards[hand_number][i] == 11 and total > 21:
            person_cards[hand_number][i] = 1
            total -= 10

    return total


def start_game(example_player,example_dealer):
    """takes the player and the dealer cards as input, and give the player 2 cards and the dealer 1. Also return the
    total of the dealer's card"""
    get_card(example_player, 0)
    get_card(example_player, 0)
    get_card(example_dealer, 0)
    dealer_total = example_dealer[0][0]
    # print(f"Your cards are {example_player[0]} for a total of {example_player[0][0] + example_player[0][1]}.")
    # print(f"The dealer is showing a {example_dealer[0]} for a total of {example_dealer[0][0]}.")
    return dealer_total


def split(person_cards, hand_number):
    """takes the persons cards and the hand number as inputs, and creates two seperate hands using the 2 cards from the
    initial hand"""
    first_card = [person_cards[hand_number][0]]
    second_card = [person_cards[hand_number][1]]
    person_cards.append(first_card)
    person_cards.append(second_card)

    length = len(person_cards)

    get_card(person_cards,length-2)
    get_card(person_cards,length-1)

    del person_cards[hand_number]


def has_eleven(list):
    """Takes a list of cards as input, and return True if one of the cards is an eleven"""
    length = len(list)
    for i in range(0, length):
        if list[i] == 11:
            return True
    return False

def dealer_strategy(dealer_sum, dealer_cards, strategy):
    """modelling the dealer strategy"""

    eleven = has_eleven(dealer_cards[0])

    if strategy == 1:
        while dealer_sum <= 16:
            dealer_sum = get_card(dealer_cards,0)

    elif strategy == 2:
        while dealer_sum <= 16:
            dealer_sum = get_card(dealer_cards,0)
            eleven = has_eleven(dealer_cards[0])
        if dealer_sum == 17 and eleven:
            dealer_sum = get_card(dealer_cards,0)

    return dealer_sum

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def strategy_split(person_cards, dealer_sum, hand_number):
    """models the splitting strategy"""
    if person_cards[hand_number][0] == person_cards[hand_number][1]:
        if person_cards[hand_number][0] == 9 and dealer_sum in (2,3,4,5,6,8,9):
            return "yes"
        elif person_cards[hand_number][0] == 8:
            return "yes"
        elif person_cards[hand_number][0] == 7 and dealer_sum in (2,3,4,5,6,7):
            return "yes"
        elif person_cards[hand_number][0] == 6 and dealer_sum in (3,4,5,6):
            return "yes"
        elif person_cards[hand_number][0] == 4 and dealer_sum in (5,6):
            return "yes"
        elif person_cards[hand_number][0] == 3 and dealer_sum in (4,5,6,7):
            return "yes"
        elif person_cards[hand_number][0] == 2 and dealer_sum in (4,5,6,7):
            return "yes"
        else:
            return "no"
    elif person_cards[hand_number][0] == 1 and person_cards[hand_number][1] == 11:
        person_cards[hand_number][0] = 11
        return "once"
    else:
        return "no"

def strategy_normal(person_cards, player_sum, dealer_sum, hand_number):
    """modelling the optimal player strategy"""
    eleven = has_eleven(person_cards[hand_number])

    # this forces players to stop taking cards after they split aces
    if len(person_cards) == 2 and person_cards[hand_number][0] == 11:
        return "stand"

    elif eleven:
        if player_sum[hand_number] in (13,14) and dealer_sum in (2,3,4,7,8,9,10,11):
            return "hit"
        elif player_sum[hand_number] in (13,14) and dealer_sum in (5,6) and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] in (13,14) and dealer_sum in (5,6) and len(person_cards[hand_number]) >2:
            return "hit"
        elif player_sum[hand_number] in (15,16) and dealer_sum in (2,3,7,8,9,10,11):
            return "hit"
        elif player_sum[hand_number] in (15,16) and dealer_sum in (4,5,6) and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] in (15, 16) and dealer_sum in (4, 5, 6) and len(person_cards[hand_number]) > 2:
            return "hit"
        elif player_sum[hand_number] == 17 and dealer_sum in (2,7,8,9,10,11):
            return "hit"
        elif player_sum[hand_number] == 17 and dealer_sum in (3,4,5,6) and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] == 17 and dealer_sum in (3,4,5,6) and len(person_cards[hand_number]) > 2:
            return "hit"
        elif player_sum[hand_number] == 18 and dealer_sum in (2,3,4,5,6) and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] == 18 and dealer_sum in (2,3,4,5,6) and len(person_cards[hand_number]) > 2:
            return "hit"
        elif player_sum[hand_number] == 18 and dealer_sum in (7,8):
            return "stand"
        elif player_sum[hand_number] == 18 and dealer_sum in (9,10,11):
            return "hit"
        elif player_sum[hand_number] == 19 and dealer_sum in (2,3,4,5,7,8,9,10,11):
            return "stand"
        elif player_sum[hand_number] == 19 and dealer_sum == 6 and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] == 19 and dealer_sum == 6 and len(person_cards[hand_number]) > 2:
            return "hit"
        elif player_sum[hand_number] in (20,21):
            return "stand"
    else:
        if player_sum[hand_number] in (4,5,6,7,8):
            return "hit"
        elif player_sum[hand_number] == 9 and dealer_sum in (2,7,8,9,10,11):
            return "hit"
        elif player_sum[hand_number] == 9 and dealer_sum in (3,4,5,6) and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] == 9 and dealer_sum in (3,4,5,6) and len(person_cards[hand_number]) > 2:
            return "hit"
        elif player_sum[hand_number] == 10 and dealer_sum in (2,3,4,5,6,7,8,9) and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] == 10 and dealer_sum in (2,3,4,5,6,7,8,9) and len(person_cards[hand_number]) > 2:
            return "hit"
        elif player_sum[hand_number] == 10 and dealer_sum in (10, 11):
            return "hit"
        elif player_sum[hand_number] == 11 and len(person_cards[hand_number]) == 2:
            return "double"
        elif player_sum[hand_number] == 11 and len(person_cards[hand_number]) > 2:
            return "hit"
        elif player_sum[hand_number] == 12 and dealer_sum in (2,3,7,8,9,10,11):
            return "hit"
        elif player_sum[hand_number] == 12 and dealer_sum in (4,5,6):
            return "stand"
        elif player_sum[hand_number] in (13,14,15,16) and dealer_sum in (2,3,4,5,6):
            return "stand"
        elif player_sum[hand_number] in (13,14,15,16) and dealer_sum in (7,8,9,10,11):
            return "hit"
        elif player_sum[hand_number] == 17:
            return "stand"
        elif player_sum[hand_number] in (18,19,20,21):
            return "stand"


def data_money(row):
    """recording the monetary outcome of a hand"""
    if row['last_action'] == "double" and row['result'] == "W":
        return 20
    elif row['last_action'] == "double" and row['result'] == "L":
        return -20
    elif row['data_split'] == True and row['hand_sum_start'] == 21 and row['result'] == "W":
        return 10
    elif row['hand_sum_start'] == 21 and row['result'] == "W":
        return 15
    elif row['result'] == "W":
        return 10
    elif row['result'] == "L":
        return -10
    else:
        return 0

