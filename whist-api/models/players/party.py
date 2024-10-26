from pydantic import UUID5, BaseModel

from typing import Optional

class Party(BaseModel):
    """A game is simply an id. Other tables reference to here."""
    gameId: UUID5
    player1: Optional[UUID5] 
    player2: Optional[UUID5]
    player3: Optional[UUID5]
    player4: Optional[UUID5]