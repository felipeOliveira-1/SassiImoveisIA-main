from fastapi import FastAPI, HTTPException
import os
import json
from pydantic import BaseModel
from typing import List, Union
from pydantic import BaseModel, HttpUrl
from typing import List

app = FastAPI()

class ContentItem(BaseModel):
    id_imovel: int
    numero_chave: str
    tipo_imovel: str
    finalidade_imovel: str
    transacao: str
    valor_locacao: float
    valor_iptu: float
    area: float
    valor_condominio: float
    descricao: str
    Detalhes: List[str]
    bairro: str
    cidade: str
    cep: str
    sala: int
    quarto: int
    banheiro: int
    cozinha: int
    vagas_garagem: int
    destaque: str
    fotos: Union[List[HttpUrl], HttpUrl] 

# Assuming casa_locacao is the main category like 'imoveis_locacao'
@app.get("/casa_locacao/{file_name}")
async def read_imovel(file_name: str):
    full_path = os.path.join("casa_locacao", file_name)
    if not os.path.exists(full_path):
        return {"error": "File not found", "path": full_path}

    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        content_items = [ContentItem(**item) for item in data]
        return [item.dict() for item in content_items]
    except Exception as e:
        return {"error": "Error parsing JSON", "message": str(e)}


