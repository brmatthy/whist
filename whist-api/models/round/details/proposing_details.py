from typing import Optional, Annotated
from pydantic import UUID5, BaseModel, Field

from models.round import RoundType
from models.cards import Suit

class ProposingDetails(BaseModel):
    """Model representing the poroposition of a single player for a round in a game."""
    gameId: UUID5
    roundId: Annotated[int, Field(ge=1)]
    playerId: UUID5
    round_type: RoundType
    trump: Optional[Suit]
    count: Annotated[int, Field(ge=0)]