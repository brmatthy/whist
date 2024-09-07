from enum import Enum
from pydantic import BaseModel

class Suit(str, Enum):
    """Enum to represent all possible suits"""
    HEARTS = "HEARTS"
    DIAMONDS = "DIAMONDS"
    CLUBS = "CLUBS"
    SPADES = "SPADES"