from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item, query: int):
    item.name = item.name.capitalize()
    item_dict = {"item_id": item_id, **item.dict()}
    item_dict.update({"query": query})
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    print("item: ", item_dict)
    return item_dict


@app.get("/req_body_items/{user_id}/{item_id}")
async def req_body_get_item(user_id: int, item_id: int):
    return {"user_id": user_id, "item_id": item_id}
