from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Sherk(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    color: str
    species: str
    photo: str
    catchphrase: str

class SherkUpdate(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    color: str 
    species: str 
    photo: str 
    catchphrase: str 








