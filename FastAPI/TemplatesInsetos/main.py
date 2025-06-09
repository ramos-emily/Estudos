from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="API dos Insetos")
app.include_router(api_router, prefix=settings.API_V1_STR)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":

    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)