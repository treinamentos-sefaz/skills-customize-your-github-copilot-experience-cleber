"""
FastAPI REST API - Starter Code
Este é um arquivo base para começar a construir sua API REST com FastAPI.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

# Inicializar a aplicação FastAPI
app = FastAPI(
    title="Item Management API",
    description="Uma API para gerenciar items",
    version="1.0.0"
)

# TODO: Defina seu modelo Pydantic Item aqui
# Deve incluir: name, description, price, tax


# TODO: Crie um armazenamento em memória para seus items
# Sugestão: use um dicionário com IDs como chaves


@app.get("/")
def read_root():
    """Endpoint raiz que retorna uma mensagem de boas-vindas"""
    # TODO: Implemente este endpoint
    pass


# TODO: Implemente os endpoints das tarefas aqui
# GET /items/ - retorna lista de todos os items
# POST /items/ - cria um novo item
# GET /items/{item_id} - retorna um item específico
# PUT /items/{item_id} - atualiza um item
# DELETE /items/{item_id} - deleta um item
