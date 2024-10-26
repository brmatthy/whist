from typing_extensions import Annotated
from pydantic import UUID5, BaseModel, Field

class Player(BaseModel):
    """Pydantic model that represents a player.
    
    :field id: A unique identifier identifying the player
    :type id: UUID5
    :field name: The name of the player
    :type id: Annotated[str, Field(pattern=r'[A-Z][A-Za-z0-9]*')]
    """
    id: UUID5 
    name: Annotated[str, Field(pattern=r'[A-Z][A-Za-z0-9]*')]
    # currently no security is needed as it is a hobby project
    # may be fun to implement in the future