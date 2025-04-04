from fastapi import FastAPI, HTTPException, status, Response, Depends, Query
from typing import Optional, Any, Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import Sherk, SherkUpdate


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI(title="API sherk", version="0.0.1", description="Api do sherk porque eu gosto muito")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def raiz():
    return{"funcionaporfavorveir"}


#listar
@app.get("/sherks", description="Retorna os personagens do banco imaginario")
async def get_sherks(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100, ) -> list[Sherk]:
    sherks = session.exec(select(Sherk).offset(offset).limit(limit)).all()
    return sherks



@app.get("/sherks/{sherk_id}")
async def get_sherk(sherk_id: int, session: SessionDep) -> Sherk:
    sherk = session.get(Sherk, sherk_id)
    if not sherk:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")
    return sherk


@app.post("/sherks", status_code=status.HTTP_201_CREATED)
async def post_sherk(sherk: Sherk, session: SessionDep) -> Sherk:
    session.add(sherk)
    session.commit()
    session.refresh(sherk)
    return sherk
  
#NAO TA FUNCIONANDO ISSO AQUI!!!!

# @app.patch("/sherks/{sherk_id}", response_model=Sherk)
# def update_sherk(sherk_id: int, sherk_update: SherkUpdate, session = Depends(get_session)):
#     sherk_db = session.get(Sherk, sherk_id)
#     if not sherk_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")
#     sherk_data = SherkUpdate.model_dump(exclude_unset=True)
#     for key, value in sherk_data.items():
#         setattr(sherk, key, value)
#     session.add(sherk_db)
#     session.commit()
#     session.refresh(sherk_db)
#     return sherk_db



@app.delete("/sherks/{sherk_id}")
async def delete_sherk(sherk_id: int, session: SessionDep):
    sherk = session.get(Sherk, sherk_id)
    if not sherk:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")
    session.delete(sherk)
    session.commit()
    return {"ok": True}

    

