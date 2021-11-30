from typing import Optional, Set, List, Dict

from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    """Object Image with specified HttpUrl type."""
    name: str
    url: HttpUrl


class Item(BaseModel):
    """
    Model with set data.
    Use Image object as optional attribute.
    images attribute has optional list of Image objects.
    """
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    """Model Offer with required list of Items."""
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., description="Body item with data")):
    """
    Example data for PUT:
    {
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    },
    "images": [
    {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    },
    {
        "url": "http://example.com/dave.jpg",
        "name": "The Baz"
    }
    ]
    }
    """

    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers/")
async def create_offer(offer: Offer):
    """Create object Offer with deeply nested models."""
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    for image in images:
        print(image.name)
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    """
    Data from request body will be converted to key(int) value(float) json format, so the key can be a string but
    after conversion it must be valid integer.
    """

    return weights
