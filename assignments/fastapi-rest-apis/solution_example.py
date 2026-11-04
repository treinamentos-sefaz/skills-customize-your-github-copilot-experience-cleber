"""
FastAPI REST API - Exemplo de Solução Completa
Este arquivo demonstra uma solução completa para todas as tarefas.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(
    title="Item Management API",
    description="Uma API para gerenciar items",
    version="1.0.0"
)


# Modelo Pydantic para validação
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    tax: Optional[float] = Field(None, ge=0)


# Armazenamento em memória
items_db = {}
next_item_id = 1


@app.get("/")
def read_root():
    """Endpoint raiz que retorna uma mensagem de boas-vindas"""
    return {
        "message": "Bem-vindo à Item Management API",
        "version": "1.0.0"
    }


@app.get("/items/", response_model=List[dict])
def list_items():
    """Retorna a lista de todos os items"""
    return [
        {"id": item_id, **item.dict()}
        for item_id, item in items_db.items()
    ]


@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    """Cria um novo item e retorna com ID"""
    global next_item_id
    item_id = next_item_id
    next_item_id += 1
    items_db[item_id] = item
    return {"id": item_id, **item.dict()}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retorna um item específico pelo ID"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item com ID {item_id} não encontrado"
        )
    return {"id": item_id, **items_db[item_id].dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Atualiza um item existente"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item com ID {item_id} não encontrado"
        )
    items_db[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """Deleta um item"""
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item com ID {item_id} não encontrado"
        )
    del items_db[item_id]
    return None
