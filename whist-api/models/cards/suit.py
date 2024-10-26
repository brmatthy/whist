from enum import Enum

class Suit(str, Enum):
    """Enum to represent all possible suits"""
    HEARTS = "HEARTS"
    DIAMONDS = "DIAMONDS"
    CLUBS = "CLUBS"
    SPADES = "SPADES"