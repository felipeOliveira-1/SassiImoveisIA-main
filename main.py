from fastapi import FastAPI, HTTPException
import os
import json

app = FastAPI()

base_dir = "sassiImoveisIA-main"

@app.get("/{transaction_type}/{id}/")
async def read_imovel(transaction_type: str, id: str):
    if transaction_type not in ["imoveis_locacao", "imoveis_venda"]:
        raise HTTPException(status_code=404, detail="Transaction type not found")
    
    file_path = os.path.join(base_dir, transaction_type, id, f"{id}.json")
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data
