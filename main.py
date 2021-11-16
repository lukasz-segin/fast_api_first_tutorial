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


@app.get("/books/{category_name}")
async def book_category_description(category_name: BookCategory):
    if category_name == BookCategory.sci_fi:
        return {"category_name": category_name.value, "message": "I like to read those kind of books."}
    if category_name.value == 'kryminał':
        return {"category_name": category_name, "message": "I don't read criminals."}
    return {"category_name": category_name, "message": "I don't like to read sensation books."}


@app.get("/files/{file_path:path}")
# file_path: /home/johndoe/myfile.txt
async def get_file(file_path: str):
    return {"file_path": f'/{file_path}'}
