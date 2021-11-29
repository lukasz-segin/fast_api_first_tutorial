from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=4, max_length=30, regex="^Item",)):
    """q is optional"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items1/")
async def read_items(q: Optional[str] = Query(None, min_length=4, max_length=30,)):
    """q is optional"""
    results = {"items1": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items2/")
async def read_items(q: str = Query(..., min_length=4, max_length=30,)):
    """
    q is required.
    When you need to declare a value as required while using Query, you can use ... as the first argument
    """

    results = {"items1": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items3/")
# http://localhost:8000/items3/?q=foo&q=bar
async def read_items(q: Optional[List[str]] = Query(None,)):
    """When you define a query parameter explicitly with Query you can also declare it to receive a list of values,
    or said in other way, to receive multiple values."""

    query_items = {"q": q}
    return query_items


@app.get("/items4/")
async def read_items(q: List[int] = Query([1, 2],)):
    """And you can also define a default list of values if none are provided
    The list items are validated by int type."""

    query_items = {"q": q}
    return query_items


@app.get("/items5/")
# http://localhost:8000/items5/?q=aaa&q=1
async def read_items(q: list = Query([],)):
    """You can also use list directly instead of List[str].
    But there is no validation."""

    query_list = {"q": q}
    return query_list


@app.get("/items6/")
# http://localhost:8000/items6/?super-item-query=fixedquery
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="super-item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
    )
):
    """Imagine that you want the parameter to be super-item-query"""

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
