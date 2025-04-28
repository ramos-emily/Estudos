from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Shrek(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    color: str
    species: str
    photo: str
    catchphrase: str

class ShrekUpdate(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    color: str 
    species: str 
    photo: str 
    catchphrase: str 








