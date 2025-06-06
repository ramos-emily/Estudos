from core.configs import settings
from core.database import engine
from models import all_models



async def create_tables() -> None:
    print("criando tabelas no banco")

    async with engine.begin() as conn:

        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)

    print("criou tabelaaaaaaaa")

if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())
