from fastapi import APIRouter
from api.v1.endpoints import inseto

api_router = APIRouter()
api_router.include_router(inseto.router, prefix="/inseto", tags=["Inseto"] ) 