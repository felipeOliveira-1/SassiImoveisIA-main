from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json


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
    Detalhes: list
    bairro: str
    cidade: str
    cep: str
    sala: int
    quarto: int
    banheiro: int
    cozinha: int
    vagas_garagem: int
    destaque: str
    fotos: list

base_dir = "sassiImoveisIA-main"

@app.get("/{transaction_type}/{dir_name}/{file_name}")
async def read_imovel(transaction_type: str, dir_name: str, file_name: str):
    full_path = os.path.join(base_dir, transaction_type, dir_name, file_name)
    if not os.path.exists(full_path):
        return {"error": "File not found", "path": full_path}

    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        content_item = ContentItem(**data)
        return content_item.dict()
