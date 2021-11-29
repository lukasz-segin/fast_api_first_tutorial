from fastapi import FastAPI, Query, Path, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}/")
async def update_item(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: Optional[str] = None,
        item: Optional[Item] = None,
):
    """
    Function for PUT method with required item_id and optional q and Item object
    Example body:
    {
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
    }
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body(..., gt=10),):
    """
    Usage of multiple Body parameters (Item and User) and added single parameter to Body (importance) using Body method.
    Example data:
    {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
    }
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.put("/items3/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    """
    Make Fast API to expect request Body data with key (item), so input data will be like:
    {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
    }
    """
    results = {"item_id": item_id, "item": item}
    return results
