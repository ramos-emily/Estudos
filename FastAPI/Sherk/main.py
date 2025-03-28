from fastapi import FastAPI, HTTPException, status, Response, Depends
from typing import Optional, Any
from models import Sherk

app = FastAPI()

def fake_db():
    try:
        print("Conectando")
    finally:
        print("Saindo...")

characters = {
    1: {
        "name": "Sherk",
        "color": "Green",
        "species": "Ogre",
        "photo": "https://uploads.jovemnerd.com.br/wp-content/uploads/2023/03/vitrine_shrek_e_mais_animacoes_dreamworks_deixarao_netflix_nerdbunker__2z154j.jpg?ims=1210x544/filters:quality(75)",
        "catchphrase": "Cebola tem camadas!",
    },
    2: {
        "name": "Burro",
        "color": "Gray",
        "species": "donkey",
        "photo": "https://fly.metroimg.com/upload/q_85,w_700/https://uploads.metroimg.com/wp-content/uploads/2024/06/24163743/Shrek-Burro-Spin-Off.jpg",
        "catchphrase": "Quando tudo isso acabar vou precisar de terapia, olha só meu olho piscando ;(",
    },
    3: {
        "name": "Fiona",
        "color": "Green",
        "species": "Ogre",
        "photo": "https://platform.polygon.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/22512340/maxresdefault.jpg?quality=90&strip=all&crop=7.8125%2C0%2C84.375%2C100&w=1200",
        "catchphrase": "A noite de um dia, de dia de outro",
    },
    4: {
        "name": "Gato de botas",
        "color": "Orange",
        "species": "Cat",
        "photo": "https://queenbi.wordpress.com/wp-content/uploads/2010/07/gordo.jpg",
        "catchphrase": "Sou eu...",
    }
}

@app.get("/")
async def raiz():
    return{"funcionaporfavorveir"}

@app.get("/characters", description="Retorna os personagens do banco imaginario")
async def get_characters(db: Any = Depends(fake_db)):
    return characters

@app.get("/characters/{character_id}")
async def get_character(character_id: int):
    try:
        character = characters[character_id]
        return character
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")

# @app.post("/characters", status_code=status.HTTP_201_CREATED)
# async def post_character(character: Optional[characters] = None):
#     next_id = len(characters) + 1
#     characters[next_id] = character
#     del character.id
#     return character

@app.put("/characters/{character_is}", status_code=status.HTTP_202_ACCEPTED)
async def put_character(character_id: int, character):
    if character_id in characters:
        characters[character_id] = character
        character_id = character_id
        del character_id
        return character
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")

@app.delete("/characters/{character_id}")
async def delete_character(character_id: int):
    if character_id in characters:
        del characters[character_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Que personagem se ta procurando fi, tem esse ai não")

