from typing import Optional
from pydantic import BaseModel

class Sherk(BaseModel):
    id: Optional[int] = None
    name: str
    color: str
    species: str
    photo: str
    catchphrase: str
    

