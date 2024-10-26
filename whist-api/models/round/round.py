from typing import Annotated, Union
from pydantic import UUID5, BaseModel
from pydantic.fields import Field

from .round_phase import RoundPhase

class Round(BaseModel):
    """Pydantic model that represents a single round.
    """
    gameId: UUID5
    id: Annotated[int, Field(le=1)]
    phase: RoundPhase
    