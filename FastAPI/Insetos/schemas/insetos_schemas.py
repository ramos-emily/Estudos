from typing import Optional
from pydantic import BaseModel as SCBaseModel

class InsetosSchema(SCBaseModel):

    id:Optional[int] = None
    name: int
    lifetime: int 
    photo: str
    size: float
    diet: str
    extinct: bool 
    curiosity: str

    class Config:
        orm_mode = True

class InsetosSchemaSenha(InsetosSchema):
    password: int
    