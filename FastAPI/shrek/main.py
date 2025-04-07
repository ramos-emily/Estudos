from fastapi import FastAPI, HTTPException, status, Response, Depends, Query, Request
from typing import Optional, Any, Annotated
from fastapi.templating import Jinja2Templates
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import Shrek, ShrekUpdate
from fastapi.staticfiles import StaticFiles


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


app = FastAPI(title="API shrek", version="0.0.1", description="Api do shrek porque eu gosto muito")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def raiz(request: Request, session: SessionDep):
    shreks = session.exec(select(Shrek)).all() 
    return templates.TemplateResponse("home.html", {"request": request, "shreks": shreks})


@app.get("/shreks")
async def get_shreks(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    shreks = session.exec(select(Shrek).offset(offset).limit(limit)).all()
    return shreks



@app.get("/shreks/{shrek_id}")
async def get_shrek(shrek_id: int, session: SessionDep) -> Shrek:
    shrek = session.get(Shrek, shrek_id)
    if not shrek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")
    return shrek


@app.post("/shreks", status_code=status.HTTP_201_CREATED)
async def post_sherk(shrek: Shrek, session: SessionDep) -> Shrek:
    session.add(shrek)
    session.commit()
    session.refresh(shrek)
    return shrek


@app.patch("/shreks/{sherk_id}", response_model=Shrek)
def update_sherk(sherk_id: int, sherk_update: ShrekUpdate, session: SessionDep):
    shrek_db = session.get(Shrek, sherk_id)
    if not shrek_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")
    shrek_data = sherk_update.model_dump(exclude_unset=True)
    for key, value in shrek_data.items():
        setattr(shrek_db, key, value)  
    session.add(shrek_db)
    session.commit()
    session.refresh(shrek_db)
    return shrek_db



@app.delete("/shreks/{shrek_id}")
async def delete_shrek(shrek_id: int, session: SessionDep):
    shrek = session.get(Shrek, shrek_id)
    if not shrek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")
    session.delete(shrek)
    session.commit()
    return {"ok": True}

    

