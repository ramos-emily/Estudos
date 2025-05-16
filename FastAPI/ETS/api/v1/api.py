from fastapi import APIRouter
from api.v1.endpoints import instrutor

api_router = APIRouter()
api_router.include_router(instrutor.router, prefix="/instrutor", tags=["Instrutor"] ) #tem q repetir pra todos os modelos