from fastapi import FastAPI, Query, Path
from typing import Optional

app = FastAPI()


@app.get("/items1/{item_id}")
# http://localhost:8000/item1/5?q=To%20jest%20test
async def read_items(
        item_id: int = Path(..., title="The ID of the item to get"),
        q: Optional[str] = Query(None, min_length=5)
):
    """You can declare all the same parameters as for Query."""

    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items2/")
async def read_items(q: str):
    return {"q": q}


@app.get("/items3/{item_id}")
async def read_items(item_id: int, q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items4/{item_id}/")
async def read_items(
        q: Optional[str] = Query(None, min_length=10),
        item_id: int = Path(..., title="The ID of the item to get", ge=1),
        tax: float = Query(..., title="Tax value", gt=0, lt=1)
):
    results = {"item_id": item_id, "tax:": tax}
    if q:
        results.update({"q": q})
    return results
