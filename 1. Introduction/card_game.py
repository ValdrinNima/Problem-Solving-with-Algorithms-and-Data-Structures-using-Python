import re
import numpy as np
import time


class Card:
    _ranks = {1: "Ace",
              2: 2,
              3: 3,
              4: 4,
              5: 5,
              6: 6,
              7: 7,
              8: 8,
              9: 9,
              10: 10,
              11: "Jack",
              12: "Queen",
              13: "King"
              }

    def __init__(self,  rank, suit):
        suitRegex = re.compile(
            r"spades?|clubs?|hearts?|diamonds?", re.IGNORECASE)

        if re.match(suitRegex, suit):
            self.suit = suit.lower() if suit[-1] == "s" else (suit+"s").lower()
            self.rank = Card._ranks[rank]
        else:
            raise Exception("Please enter a correct suit.")

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck():
    def __init__(self):
        self.deck = []

        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in range(1, 14):
                self.deck.append(Card(rank, suit))

    def __getitem__(self, index):
        return self.deck[index]

    def shuffle(self):
        return np.random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()

    def draw(self):
        return self.deck.pop()

    def draw_multiple(self, num=1):
        drawn_cards = []
        for _ in range(num):
            drawn_cards.append(self.deck.pop())

        return list(map(lambda x: x.__str__(), drawn_cards))

    def info(self):
        count = len(self.deck)
        num_of_clubs = len(
            [card for card in self.deck if card.suit == "clubs"])
        num_of_diamonds = len(
            [card for card in self.deck if card.suit == "diamonds"])
        num_of_hearts = len(
            [card for card in self.deck if card.suit == "hearts"])
        num_of_spades = len(
            [card for card in self.deck if card.suit == "spades"])

        print(
            f"""Count: {count}
Number of clubs: {num_of_clubs}
Number of diamonds: {num_of_diamonds}
Number of hearts: {num_of_hearts}
Number of spades: {num_of_spades}""")

    def __repr__(self):
        return f"{list(map(lambda x: x.__str__(), self.deck))}"


class Player():
    def __init__(self, name, number, hand):
        self.name = name
        self.number = number
        self.hand = hand
        self.score = 0




test_deck = Deck()
test_deck.shuffle()
print(test_deck)

print(test_deck.draw_multiple(3))
bla = test_deck[1]
print(bla)


def main():
    game_is_running = True
    while(game_is_running):
        # player_count = input("Choose the player count. (2-4)")
        print("Shuffle the deck...")
        time.sleep(2)
        



if __name__ == "__main__":
    main()
