from fastapi import FastAPI, HTTPException
import os
import json

app = FastAPI()

# Base directory inside your project where the 'imoveis' folder is located.
base_dir = "sassiImoveisIA-main"

@app.get("/{transaction_type}/{dir_name}/{file_name}")
async def read_imovel(transaction_type: str, dir_name: str, file_name: str):
    # Construct the full path to the file
    full_path = os.path.join(base_dir, transaction_type, dir_name, file_name)

    # Check if the file exists, if not, return a 404 error
    if not os.path.exists(full_path):
        return {"error": "File not found", "path": full_path}

    # Open and read the JSON file, then return its contents
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
