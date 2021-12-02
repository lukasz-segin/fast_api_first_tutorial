from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """
    Fast API will use response_model to
    - convert the output data to its type declaration,
    - validate the data,
    - add a JSON Schema for the response, in the OpenAPI path operation,
    - will be used by the automatic documentation systems,
    - limit the output data to that of the model.
    """

    return item


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    """
    Usage of two models to insert data with password (UserIn)
    and model to return data without password (UserOut).
    Especially to ensure private data is filtered out
    """

    return user


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    """
    Use the response_model_exclude_unset parameter equals True to omit the values which were not actually store.
    For example, if you have models with many optional attributes in a NoSQL database,
    but you don't want to send very long JSON responses full of default values.
    """
    return items[item_id]
