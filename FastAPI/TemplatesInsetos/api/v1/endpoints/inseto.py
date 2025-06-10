from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.all_models import InsetoModel
from schemas.insetos_schemas import InsetoSchema, InsetoUpdateSchema
from core.deps import get_session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(InsetoModel))
        insetos = result.scalars().all()
    return templates.TemplateResponse("home.html", {"request": request, "insetos": insetos})

@router.get("/cadastro", response_class=HTMLResponse)
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post("/home", status_code=status.HTTP_201_CREATED)
async def post_inseto(
    request: Request,
    name: str = Form(...),
    lifetime: int = Form(...),
    photo: str = Form(""),
    size: float = Form(...),
    diet: str = Form(...),
    extinct: bool = Form(False),
    curiosity: str = Form(""),
    db: AsyncSession = Depends(get_session)
):
    novo_inseto = InsetoModel(
        name=name,
        lifetime=lifetime,
        photo=photo,
        size=size,
        diet=diet,
        extinct=extinct,
        curiosity=curiosity
    )
    db.add(novo_inseto)
    await db.commit()
    return RedirectResponse(url="/api/v1/inseto/home?message=Inseto cadastrado com sucesso!", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/home/delete/{inseto_id}")
async def delete_inseto(inseto_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(InsetoModel).filter(InsetoModel.id == inseto_id))
        inseto_del = result.scalar_one_or_none()
        if inseto_del:
            await session.delete(inseto_del)
            await session.commit()
        else:
            raise HTTPException(detail="Inseto não encontrado", status_code=status.HTTP_404_NOT_FOUND)
    return RedirectResponse(url="/api/v1/inseto/home?message=Inseto excluído com sucesso!", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/home/edit/{inseto_id}", response_class=HTMLResponse)
async def get_edit_form(inseto_id: int, request: Request, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(InsetoModel).filter(InsetoModel.id == inseto_id))
        inseto = result.scalar_one_or_none()
        if not inseto:
            raise HTTPException(detail="Inseto não encontrado", status_code=status.HTTP_404_NOT_FOUND)
    return templates.TemplateResponse("edit_inseto.html", {"request": request, "inseto": inseto})

@router.post("/home/edit/{inseto_id}")
async def put_inseto_form(
    inseto_id: int,
    name: str = Form(...),
    lifetime: int = Form(...),
    photo: str = Form(""),
    size: float = Form(...),
    diet: str = Form(...),
    extinct: bool = Form(False),
    curiosity: str = Form(""),
    db: AsyncSession = Depends(get_session)
):
    async with db as session:
        result = await session.execute(select(InsetoModel).filter(InsetoModel.id == inseto_id))
        inseto = result.scalar_one_or_none()
        if not inseto:
            raise HTTPException(detail="Inseto não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        inseto.name = name
        inseto.lifetime = lifetime
        inseto.photo = photo
        inseto.size = size
        inseto.diet = diet
        inseto.extinct = extinct
        inseto.curiosity = curiosity
        await session.commit()
    return RedirectResponse(url="/api/v1/inseto/home?message=Inseto atualizado com sucesso!", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/", response_model=List[InsetoSchema])
async def get_inseto(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InsetoModel)
        result = await session.execute(query)
        return result.scalars().all()

@router.get("/{inseto_id}", response_model=InsetoSchema)
async def get_inseto(inseto_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InsetoModel).filter(InsetoModel.id == inseto_id)
        result = await session.execute(query)
        inseto = result.scalar_one_or_none()
        if inseto:
            return inseto
        else:
            raise HTTPException(detail="Inseto não encontrado", status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{inseto_id}", response_model=InsetoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_inseto(inseto_id: int, inseto: InsetoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(InsetoModel).filter(InsetoModel.id == inseto_id))
        inseto_up = result.scalar_one_or_none()
        if inseto_up:
            for key, value in inseto.dict().items():
                setattr(inseto_up, key, value)
            await session.commit()
            return inseto_up
        else:
            raise HTTPException(detail="Inseto não encontrado", status_code=status.HTTP_404_NOT_FOUND)

@router.patch("/{inseto_id}", response_model=InsetoSchema, status_code=status.HTTP_202_ACCEPTED)
async def patch_inseto(inseto_id: int, inseto: InsetoUpdateSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(InsetoModel).filter(InsetoModel.id == inseto_id))
        inseto_db = result.scalar_one_or_none()
        if not inseto_db:
            raise HTTPException(detail="Inseto não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        update_data = inseto.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(inseto_db, key, value)
        await session.commit()
        await session.refresh(inseto_db)
        return inseto_db
