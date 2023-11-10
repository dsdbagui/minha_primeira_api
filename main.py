from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Olá": "Mundo"}

produtos = [
    {
        "id": 1,    
        "nome": "Iphone14",
        "descricao": "Descrição do produto 1",
        "preco": 5000.00
    },
        {
        "id": 1,    
        "nome": "Iphone14",
        "descricao": "Descrição do produto 1",
        "preco": 5000.00
    },
        {
        "id": 2,    
        "nome": "PS5",
        "descricao": "Descrição do produto 2",
        "preco": 12000.00
    },
            {
        "id": 3,    
        "nome": "Workshop",
        "descricao": "Workshop Sábado",
        "preco": 100.00
    }
]

@app.get("/produtos")
def retorna_a_lista_de_produtos():
    return produtos