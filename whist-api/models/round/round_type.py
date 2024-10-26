from enum import Enum

class RoundType(str, Enum):
    """Enum to represent all round types"""
    ROUND_PASS = "ROUND_PASS"
    
    TEAM = "TEAM"
    SOLO = "SOLO"
    
    TROEL = "TROEL"
    
    ABONDANCE = "ABONDANCE"
    
    CARD_BLANCHE = "CARD_BLANCHE"
    
    MISERY = "MISERY"
    NAKED_MISERY = "NAKED_MISERY"
    
    SOLO_SMART = "SOLO_SMART"