from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.configs import settings

class ClasseModel(settings.DBBaseModel):
    __tablename__ = "classes"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100), nullable=False)

    insetos = relationship("InsetoModel", back_populates="classe")
