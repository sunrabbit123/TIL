from typing import Optional, Set

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["items"],
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax, and a set of unique tags",
)
async def create_item(item: Item):
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "FOO", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]
