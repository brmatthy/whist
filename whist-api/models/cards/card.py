from typing_extensions import Annotated
from pydantic import BaseModel, Field

from .suit import Suit

class Card(BaseModel):
    """Pydantic model that represents a card
    
    :field suit: The suite of the card
    :type suit: Suit
    :field rank: The rank of the card
    :type rank: Annotated[int, Field(ge=0, le=13)]
    """
    suit: Suit
    rank: Annotated[int, Field(ge=0, le=13)]