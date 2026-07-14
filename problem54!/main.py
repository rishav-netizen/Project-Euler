p1_sc = 0
p2_sc = 0

value = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIRS = 3
THREE_OF_A_KIND = 4
STRAIGHT = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH = 10

with open("0054_poker.txt", "r") as file:
    for line in file:
        line = line.strip() # reduces len by 1 since it removes the \n

        l = len(line)
        l1 = int(l/2)
        l2 = int(l/2) + 1

        p1_hand = line[:l1]
        p2_hand = line[l2:]

        p1_cards = p1_hand.split(" ")
        p2_cards = p2_hand.split(" ")

        suit_count_p1 = {
            'H' : 0,
            'D' : 0,
            'S' : 0,
            'C' : 0
        } 

        numerical_count_p1 = {
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            'T': 0,
            'J': 0,
            'Q': 0,
            'K': 0,
            'A': 0
        }

        suit_count_p2 = {
            'H' : 0,
            'D' : 0,
            'S' : 0,
            'C' : 0
        } 

        numerical_count_p2 = {
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            'T': 0,
            'J': 0,
            'Q': 0,
            'K': 0,
            'A': 0
        }
        
        p1_card_val = 0
        p2_card_val = 0

        p1_hand_val = 0
        p2_hand_val = 0

        for card in p1_cards:
            p1_card_val += value[card[0]]
            suit_count_p1[card[1]] += 1
            numerical_count_p1[card[0]] += 1

        for card in p2_cards:
            p2_card_val += value[card[0]]
            suit_count_p2[card[1]] += 1
            numerical_count_p2[card[0]] += 1
        
        # gives list of number of cards excluding zero ones
        p1_signature = sorted([count for count in numerical_count_p1.values() if count != 0], reverse=True)
        p2_signature = sorted([count for count in numerical_count_p2.values() if count != 0], reverse=True)

        # card list in form of their numerical value and this is already ascending sorted
        p1_val_cards = [value[count] for count in numerical_count_p1.keys() if numerical_count_p1[count] != 0] 
        p2_val_cards = [value[count] for count in numerical_count_p2.keys() if numerical_count_p2[count] != 0] 

        if 5 in suit_count_p1.values() and (p1_val_cards == [10, 11, 12, 13, 14]):
            p1_hand_val = ROYAL_FLUSH
        elif (5 in suit_count_p1.values()) and (p1_signature == [1, 1, 1, 1, 1]) and (p1_val_cards[-1] - p1_val_cards[0] == 4): # for consecutive sorted sequence max - min would return (length - 1) = 4 since 5 cards
            p1_hand_val = STRAIGHT_FLUSH
        elif 4 in numerical_count_p1.values(): 
            p1_hand_val = FOUR_OF_A_KIND
        elif (3 in numerical_count_p1.values()) and (2 in numerical_count_p1.values()): 
            p1_hand_val = FULL_HOUSE
        elif 5 in suit_count_p1.values():
            p1_hand_val = FLUSH
        elif (p1_signature == [1, 1, 1, 1, 1]) and (p1_val_cards[-1] - p1_val_cards[0] == 4):
            p1_hand_val = STRAIGHT
        elif 3 in numerical_count_p1.values():
            p1_hand_val = THREE_OF_A_KIND
        elif p1_signature == [2,2,1]:
            p1_hand_val = TWO_PAIRS
        elif 2 in numerical_count_p1.values():
            p1_hand_val = ONE_PAIR
        else:
            p1_hand_val = HIGH_CARD

        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        if 5 in suit_count_p2.values() and (p2_val_cards == [10, 11, 12, 13, 14]):
            p2_hand_val = ROYAL_FLUSH
        # Straight Flush: All cards are consecutive values of same suit.
        elif (5 in suit_count_p2.values()) and (p2_signature == [1, 1, 1, 1, 1]) and (p2_val_cards[-1] - p2_val_cards[0] == 4): # for consecutive sorted sequence max - min would return (length - 1) = 4 since 5 cards
            p2_hand_val = STRAIGHT_FLUSH
        # Four of a Kind: Four cards of the same value.
        elif 4 in numerical_count_p2.values(): 
            p2_hand_val = FOUR_OF_A_KIND
        # Full House: Three of a kind and a pair.
        elif (3 in numerical_count_p2.values()) and (2 in numerical_count_p2.values()): 
            p2_hand_val = FULL_HOUSE
        # Flush: All cards of the same suit.
        elif 5 in suit_count_p2.values():
            p2_hand_val = FLUSH
        # Straight: All cards are consecutive values.
        elif (p2_signature == [1, 1, 1, 1, 1]) and (p2_val_cards[-1] - p2_val_cards[0] == 4):
            p2_hand_val = STRAIGHT
        # Three of a Kind: Three cards of the same value.
        elif 3 in numerical_count_p2.values():
            p2_hand_val = THREE_OF_A_KIND
        # Two Pairs: Two different pairs.
        elif p2_signature == [2,2,1]:
            p2_hand_val = TWO_PAIRS
        # One Pair: Two cards of the same value.
        elif 2 in numerical_count_p2.values():
            p2_hand_val = ONE_PAIR
        else:
            p2_hand_val = HIGH_CARD

        # 1. Build the list of (count, numerical_value) tuples for each player
        p1_tuples = [(count, value[card_str]) for card_str, count in numerical_count_p1.items() if count != 0]
        p2_tuples = [(count, value[card_str]) for card_str, count in numerical_count_p2.items() if count != 0]

        # 2. Sort them descending (Highest count first, highest value second)
        p1_tiebreaker = sorted(p1_tuples, reverse=True)
        p2_tiebreaker = sorted(p2_tuples, reverse=True)


        if p1_hand_val > p2_hand_val:
            p1_sc += 1
        elif p1_hand_val < p2_hand_val:
            p2_sc += 1
        else:
            if p1_tiebreaker > p2_tiebreaker:
                p1_sc += 1
            else:
                p2_sc += 1

print("Scores:")
print(f"Player 1: {p1_sc}")
print(f"Player 2: {p2_sc}")
