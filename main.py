import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player_cards = []
dealer_cards = []
player_sum = 0
dealer_sum = 0


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


def startGame():
    player_sum = getCard(player_cards)
    player_sum = getCard(player_cards)
    dealer_sum = getCard(dealer_cards)
    print(f"Dealer shows a {dealer_cards} for a total of {dealer_sum}.")
    print(f"Player shows a {player_cards} for a total of {player_sum}.")


startGame()

#################################################
### Case 1: If dealer shows a 2, 3, 4, 5 or 6 ###
#################################################

# (1) If you have a 1 or you dont have an 11, then just hit it until you get to 12




# (2) if you have 11, then keep hitting until you get to 19 (stop at 19)

#############################################
### Case 2: If dealer shows a 7 or bigger ###
#############################################

# (1) if you have a 1 or you dont have an 11, then just hit until you get to 17
# (2) if you have 11, then keep hitting until you get to 19 (stop at 19)
