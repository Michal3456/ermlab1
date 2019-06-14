class Deck():
    def __init__(self):# basic constructor
        """ Return card tables 52, unsorted """
        self.cards = ['k','w','2','3','4','5','6','7','8','9','10','j','d']
    def Deck(self) -> str:# card table
        """ Return card tables 26, unsorted """
        return ''
    def sort_deck(self) -> int:# pesudolos sorting 26 cards
        """ Return card tables 26, sorted"""
        return ''
    def shuffle(self) -> str:  # sort cards
        """ Return sorted cards """
        return ''
class Card():
    def Card(self) -> str:# basic constructor
        """ Return self<value. """
        return ''
    def get_cardID(self) -> str:# send data
        """ Return send data from the card's id """
        return ''
    def set_value_card(self, name)-> int:# setting the weight value for the card
        """ Return 0 lub -1. """
        self.__name = name
    def __le__(self, value)-> bool:# x self larger than value
        """ Return self<=value. """
        return self<=value
    def __str__(self):#
        """ Return self<value. """
        return ""
    def __lt__(self, value: int) -> bool: # self sharply smaller value
        """ Return self<value. """
        return self < value
    def __ge__(self, value: int)-> bool: # self less than value
        """ Return self>=value. """
        return self >= value
    def __gt__(self, value: int)-> bool: # self sharply bigger value
        """ Return self>value. """
        return self>value
    def __eq__(self, value: int)-> bool: # self identical with value
        """ Return self==value. """
        return self == value
class Hand():
    def Hand(self) -> str:# basic constructor
        """ Return self<value. """
        return ''
def win(count_games: int) -> str:#
    """ Return str """
    return ''
def end():#
    """ Return 0 """
def games(count_games: int)-> str:# simulation of count_games games
    """ Return string """
    return ''
