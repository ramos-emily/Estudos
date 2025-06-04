from core.configs import settings
from sqlalchemy import Column, Integer, Boolean, Float, String

class InsetoModel(settings.DBBaseModel):
    __tablename__ = "insetos"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    name: str = Column(String(256))
    lifetime: str = Column(String(256))
    photo: str = Column(String(256))
    size: float = Column(Float())
    diet: str = Column(String(256))
    extinct: bool = Column(Boolean())
    curiosity: str = Column(String(256))


    