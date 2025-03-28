from fastapi import FastAPI, HTTPException, status, Response, Depends
from typing import Optional, Any
from model import Pato

app = FastAPI(title="API ducks", version="0.0.1", description="Api de pato poruqe a yasmin é doida")

def fake_db():
    try:
        print("Conectando")
    finally:
        print("Saindo...")

patos = {
    1: {
        "nome": "Luca",
        "especie": "Pato mexicano",
        "idade": 25,
        "cor": "Branco",
        "foto": "https://domineingles.com.br/wp-content/uploads/2020/06/cair-como-um-patinho-em-ingles.jpg"
    },
    2: {
        "nome": "Perry",
        "especie": "ornitorrinco",
        "idade": 5,
        "cor": "marrom",
        "foto": "https://img.freepik.com/fotos-premium/ornitorrinco-curioso-sombrero-marron-lupa-mano_14117-455272.jpg?w=360"
    }
}

@app.get("/")
async def raiz():
    return {"ypeeeeeeeeeeeeeee!"}

@app.get("/patos", description="Retorna todos os patos que estão no banco", summary="Retorna todos os patos")
async def get_patos(db: Any = Depends(fake_db)):
    return patos

@app.get("/patos/{pato_id}")
async def get_pato(pato_id: int):
    try:
        pato = patos[pato_id]
        return pato
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe patinho com esse ID {pato_id}")

@app.post("/patos", status_code=status.HTTP_201_CREATED)
async def post_pato(pato: Optional[Pato] = None):
    next_id = len(patos) + 1
    patos[next_id] = pato
    del pato.id
    return pato

@app.put("/patos/{pato_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_pato(pato_id: int, pato: Pato):
    if pato_id in patos:
        patos[pato_id] = pato
        pato_id = pato_id
        del pato.id
        return pato
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nao existe pato com o ID {pato_id}")

@app.delete("/patos/{pato_id}")
async def delete_pato(pato_id: int):
    if pato_id in patos:
        del patos[pato_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nao existe pato com o ID {pato_id}")

@app.get("/calculadora")
async def calcular(num1: int, num2: int):
    soma = num1 + num2
    return soma

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
