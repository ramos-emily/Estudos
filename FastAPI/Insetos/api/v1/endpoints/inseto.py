from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.all_models import InsetoModel
from schemas.insetos_schemas import InsetoSchema, InsetoUpdateSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=InsetoSchema)
async def post_inseto(inseto: InsetoSchema, db: AsyncSession = Depends(get_session)):
    novo_inseto = InsetoModel(name=inseto.name, lifetime=inseto.lifetime, photo=inseto.photo, size=inseto.size, diet=inseto.diet, extinct=inseto.extinct, curiosity=inseto.curiosity)

    db.add(novo_inseto)

    await db.commit()

    return novo_inseto

@router.get("/", response_model=List[InsetoSchema])
async def get_inseto(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InsetoModel)
        result = await session.execute(query)

        insetos: List[InsetoModel] = result.scalars().all()

        return insetos

@router.get("/{inseto_id}", response_model=InsetoSchema)
async def get_inseto(inseto_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InsetoModel).filter(InsetoModel.id == inseto_id)

        result = await session.execute(query)

        inseto = result.scalar_one_or_none()

        if inseto:
            return inseto
        else:
            raise HTTPException(detail="Inseto nao incontrado", status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{inseto_id}", response_model=InsetoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_inseto(inseto_id: int, inseto: InsetoSchema, db:AsyncSession = Depends(get_session)):
        async with db as session:
            query = select(InsetoModel).filter(InsetoModel.id == inseto_id)
            result = await session.execute(query)
            inseto_up = result.scalar_one_or_none()

        if inseto_up:
            inseto_up.nome = inseto.nome
            inseto_up.idade = inseto.idade
            inseto_up.materia = inseto.materia
            inseto_up.foto = inseto.foto

            await session.commit()
            return inseto_up
        else:
            raise HTTPException(detail="Inseto nao encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
@router.patch("/{inseto_id}", response_model=InsetoSchema, status_code=status.HTTP_202_ACCEPTED)
async def patch_inseto(inseto_id: int, inseto: InsetoUpdateSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InsetoModel).filter(InsetoModel.id == inseto_id)
        result = await session.execute(query)
        inseto_db = result.scalar_one_or_none()

        if not inseto_db:
            raise HTTPException(detail="Inseto nao encontrado", status_code=status.HTTP_404_NOT_FOUND)

        update_data = inseto.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(inseto_db, key, value)

        await session.commit()
        await session.refresh(inseto_db)
        return inseto_db   


@router.delete("/{inseto_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inseto(inseto_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InsetoModel).filter(InsetoModel.id == inseto_id)
        result = await session.execute(query)
        inseto_del = result.scalar_one_or_none()
        
        if inseto_del:
            await session.delete(inseto_del)
            await session.commit()
            return Response()
        else:
            raise HTTPException(detail="Inseto nao encontrado", status_code=status.HTTP_404_NOT_FOUND)


