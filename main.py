from typing import Optional
from fastapi import FastAPI
from book import BookCategory

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/books/{book_category_name}")
async def book_category_description(book_category_name: BookCategory):
    # if category_name == BookCategory.sci_fi:
    #     return {"category_name": category_name.value, "message": "I like to read those kind of books."}
    # if category_name.value == 'kryminał':
    #     return {"category_name": category_name, "message": "I don't read criminals."}
    # return {"category_name": category_name, "message": "I don't like to read sensation books."}
    return {"category_name": category_name for category_name in BookCategory if
            category_name == book_category_name}


@app.get("/files/{file_path:path}")
# file_path: /home/johndoe/myfile.txt
async def get_file(file_path: str):
    return {"file_path": f'/{file_path}'}


# Query Parameters
fake_items_from_db = [{"item_number": number} for number in range(100)]


@app.get("/db-items/")
async def db_items(start: int = 0, limit: int = 10):
    return fake_items_from_db[start: start + limit]


@app.get("/vegetables/{item_id}")
async def get_vegetables(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "query_value": q}
    return {"item_id": item_id, "query_value": "There was no query"}


@app.get("/new_items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    print(item_id)
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
