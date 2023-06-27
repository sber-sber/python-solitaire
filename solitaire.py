# import PyQt6
from typing import Any


class Card:
    def __init__(self, suit, value) -> None:
        self._suit = suit
        self._value = value

    def get_card(self):
        return self

    def get_suit(self):
        return self._suit
    
    def get_value(self):
        return self._value

    def get_shorthand_card(self):
        return f"{self._value}{self._suit}"
    
    #todo: figure out GUI "hooks"


class Deck:
    def __init__(self) -> None:
        # hearts, diamonds, clubs, spades
        self._deck = []
        suits = ("H", "D", "C", "S")
        values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        for suit in suits:
            for value in values:
                self._deck.append(Card(suit, value))
    
    def get_deck(self):
        return self._deck
    
    def get_shorthand_deck(self):

        # pass
        shorthand_deck = []
        for card in self._deck:
            shorthand_deck.append(f"{card.get_value()}{card.get_suit()}")
                # self._value}{self._suit}"
        return shorthand_deck

    # todo: create shuffle and deal/start methods 


class GameBoard:
    def __init__(self):
        pile1 = []
        pile2 = []
        pile3 = []
        pile4 = []
        pile5 = []
        pile6 = []
        pile7 = []
        tableau = [pile1, pile2, pile3, pile4, pile5, pile6, pile7]

        draw_pile = []
        discard_pile = []

        foundation1 = []
        foundation2 = []
        foundation3 = []
        foundation4 = []


class Game():
    def __init__(self) -> None:
        pass

    


game_deck = Deck()
# print(deck.get_shorthand_deck())
# print(game_deck)

# print(game_deck.get_deck())
print(game_deck.get_shorthand_deck())
