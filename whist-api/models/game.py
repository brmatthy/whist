from pydantic import UUID5, BaseModel

class Game(BaseModel):
    """A game is simply an id. Other tables reference to here."""
    id: UUID5