from typing import Optional
from pydantic import BaseModel as SCBaseModel
from pydantic import BaseModel

class InsetoSchema(SCBaseModel):

    id:Optional[int] = None
    name: str
    lifetime: str 
    photo: str
    size: float
    diet: str
    extinct: bool 
    curiosity: str

    class Config:
        orm_mode = True

class InsetosSchemaSenha(InsetoSchema):
    password: int

class InsetoUpdateSchema(BaseModel):
    name: Optional[str] = None
    lifetime: Optional[int] = None
    photo: Optional[str] = None
    size: Optional[float] = None
    diet: Optional[str] = None
    extinct: Optional[bool] = None
    curiosity: Optional[str] = None


    