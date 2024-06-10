import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


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


def start_game(player_sum, dealer_sum, player_cards, dealer_cards):
    """this takes the player and dealer sums/cards, and then adds a card to their arrays, and returns the new sums"""
    player_sum = get_card(player_cards)
    player_sum = get_card(player_cards)
    dealer_sum = get_card(dealer_cards)

    if player_cards[0] == player_cards[1]:
        equal_cards = True
    else:
        equal_cards = False

    if player_cards[0] == 11 or player_cards[1] == 11:
        soft_hand = True
    else:
        soft_hand = False

    # print(f"Dealer shows a {dealer_cards} for a total of {dealer_sum}.")
    # print(f"Player shows a {player_cards} for a total of {player_sum}.")
    return player_sum, dealer_sum, equal_cards, soft_hand


def player_strategy(player_sum, dealer_sum, player_cards, strategy):
    """Input the plauer strategy that we want to play, and it will play it. Also returns the player_sum"""

    if strategy == 1.0:
        if dealer_sum <= 6:
            while player_sum <= 11:
                player_sum = get_card(player_cards)
        else:
            while player_sum <= 16:
                player_sum = get_card(player_cards)

    elif strategy == 2.0:
        eleven = has_eleven(player_cards)
        if dealer_sum <= 6:
            while player_sum <= 11:
                player_sum = get_card(player_cards)
                eleven = has_eleven(player_cards)
            while eleven:
                if player_sum <= 18:
                    player_sum = get_card(player_cards)
                    eleven = has_eleven(player_cards)
                else:
                    break
        else:
            while player_sum <= 16:
                player_sum = get_card(player_cards)
                eleven = has_eleven((player_cards))
            while eleven:
                if player_sum <= 18:
                    player_sum = get_card(player_cards)
                    eleven = has_eleven(player_cards)
                else:
                    break

    return player_sum


def dealer_strategy(dealer_sum, dealer_cards, strategy):

    eleven = has_eleven(dealer_cards)

    if strategy == 1:
        while dealer_sum <= 16:
            dealer_sum = get_card(dealer_cards)

    elif strategy == 2:
        while dealer_sum <= 16:
            dealer_sum = get_card(dealer_cards)
            eleven = has_eleven(dealer_cards)
        if dealer_sum == 17 and eleven:
            dealer_sum = get_card(dealer_cards)

    return dealer_sum



def record_result(player_sum, dealer_sum, money_cum):
    if player_sum > 21:
        result = "L"
        money_cum -= 15
        money_hand = -15
    elif dealer_sum > 21:
        result = "W"
        money_cum += 15
        money_hand = 15
    elif player_sum > dealer_sum:
        result = "W"
        money_cum += 15
        money_hand = 15
    elif player_sum < dealer_sum:
        result = "L"
        money_cum -= 15
        money_hand = -15
    elif player_sum == dealer_sum:
        result = "T"
        money_hand = 0
    return result, money_cum, money_hand


def split_hand(list_cards, dealer_card):
    if list_cards[0] == list_cards[1]:
        if list_cards[0] ==
