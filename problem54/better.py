class Player:
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

    def __init__(self, player_name: str, player_cards: list) -> None:
        self.name = player_name
        self.cards = player_cards
        self.score = 0
        self.hand_val = 0
        self.suit_count =  {
            'H' : 0,
            'D' : 0,
            'S' : 0,
            'C' : 0
        } 

        self.numerical_count = {
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

        for card in self.cards:
            self.suit_count[card[1]] += 1
            self.numerical_count[card[0]] += 1

        self.signature = sorted(
            [
                count 
                for count in self.numerical_count.values() 
                if count != 0
            ]
            , reverse=True
        )

        self.value_cards_list = [
            self.value[count] 
            for count in self.numerical_count.keys() 
            if self.numerical_count[count] != 0
        ]
        
        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        if 5 in self.suit_count.values() and (self.value_cards_list == [10, 11, 12, 13, 14]):
            self.hand_val = self.ROYAL_FLUSH

        # Straight Flush: All cards are consecutive values of same suit.
        elif (5 in self.suit_count.values()) and (self.signature == [1, 1, 1, 1, 1]) and (self.value_cards_list[-1] - self.value_cards_list[0] == 4): # for consecutive sorted sequence (max - min) would return (length - 1) = 4 since 5 cards
            self.hand_val = self.STRAIGHT_FLUSH

        # Four of a Kind: Four cards of the same value.
        elif 4 in self.numerical_count.values(): 
            self.hand_val = self.FOUR_OF_A_KIND

        # Full House: Three of a kind and a pair.
        elif (3 in self.numerical_count.values()) and (2 in self.numerical_count.values()): 
            self.hand_val = self.FULL_HOUSE

        # Flush: All cards of the same suit.
        elif 5 in self.suit_count.values():
            self.hand_val = self.FLUSH

        # Straight: All cards are consecutive values.
        elif (self.signature == [1, 1, 1, 1, 1]) and (self.value_cards_list[-1] - self.value_cards_list[0] == 4):
            self.hand_val = self.STRAIGHT

        # Three of a Kind: Three cards of the same value.
        elif 3 in self.numerical_count.values():
            self.hand_val = self.THREE_OF_A_KIND

        # Two Pairs: Two different pairs.
        elif self.signature == [2,2,1]:
            self.hand_val = self.TWO_PAIRS

        # One Pair: Two cards of the same value.
        elif 2 in self.numerical_count.values():
            self.hand_val = self.ONE_PAIR
        
        # High Card: Highest value card.
        else:
            self.hand_val = self.HIGH_CARD
    

        # 1. Build the list of (count, numerical_value) tuples for each player
        self.tuples = [
            (count, self.value[card_str]) 
            for card_str, count in self.numerical_count.items() 
            if count != 0
            ]
        
        # 2. Sort them descending (Highest count first, highest value second)
        self.tiebreaker = sorted(self.tuples, reverse=True)

     
    # Dunder(double underscore) Method (added this for fun lol)
    def __str__(self):
        return f"Poker Player Name: {self.name}, Score: {self.score}"

    def __repr__(self):
        return f'Instant of player obj, name="{self.name}", score: "{self.score}"'
    
    # stands for greater than, allows us to directly compare player objects in main
    def __gt__(self, other):
        if self.hand_val > other.hand_val:
            return True
        elif self.hand_val < other.hand_val:
            return False
        else:
            return self.tiebreaker > other.tiebreaker

    # in case of equality, which is not there for this problem set but still adding it
    def __eq__(self, other):
        return (self.hand_val == other.hand_val) and (self.tiebreaker == other.tiebreaker)
    
def main():
    p1_total_score = 0
    p2_total_score = 0

    with open("0054_poker.txt", "r") as file:
        for line in file:
            line = line.strip()

            l = len(line)
            l1 = int(l/2)
            l2 = int(l/2) + 1

            # string
            p1_hand = line[:l1]
            p2_hand = line[l2:]

            # list of all cards
            p1_cards = p1_hand.split(" ")
            p2_cards = p2_hand.split(" ")

            p1 = Player("Player 1", p1_cards)
            p2 = Player("Player 2", p2_cards)

            if p1 > p2:
                p1_total_score += 1
            elif p1 < p2:
                p2_total_score += 1
            else:
                print(f"Dead Tie! Split the pot.")


    print(f"Player1: {p1_total_score}")
    print(f"Player2: {p2_total_score}")
    # print(repr(p1))

if __name__ == "__main__":
    main()