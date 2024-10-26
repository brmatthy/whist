from enum import Enum

class RoundPhase(str, Enum):
    """Enum to represent all round phases"""
    PROPOSING = "PROPOSING"
    BIDDING = "BIDDING"
    PLAYING = "PLAYING"
    FINISHED = "FINISHED"