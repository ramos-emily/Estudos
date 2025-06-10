from pydantic.v1 import BaseSettings #configuraçoes gerais para facilitar
from sqlalchemy.orm import declarative_base 

class Settings(BaseSettings):
    #configurações gerais da API

    API_V1_STR: str = "/api/v1"

    # DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3309/insetos"
    DB_URL: str = "mysql+asyncmy://root:1234@127.0.0.1:3306/insetos"


    DBBaseModel = declarative_base()

class Config:
    case_sensitive = False
    env_file = "env"

settings = Settings()