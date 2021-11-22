import csv
import random
import string
from typing import Optional
from fastapi import FastAPI
from book import BookCategory

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Generation of digit code of k digits! Sorting a dictionary."""

    code = "".join(random.choices(string.digits, k=6))

    return {"item_id": item_id, "code": code}


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


# @app.get("/sorted-items/")
# async def sorted_items():
#     users = [
#         {"first_name": "Helena", "age": 39},
#         {"first_name": "Bartek", "age": 10},
#         {"first_name": "Ania", "age": 9},
#     ]
#     return {"users": users}

# """Process and Sort dictionary using function"""
#
# users = [
#     {"first_name": "Helena", "age": 39},
#     {"first_name": "Bartek", "age": 10},
#     {"first_name": "Ania", "age": 9},
# ]
#
#
# def get_user_name(users):
#     """Reading name and change letters to lower."""
#
#     return users["first_name"].lower()
#
#
# def get_sorted_dictionary(users):
#     """Sorting nesterd dictionary"""
#
#     if not isinstance(users, dict):
#         raise ValueError("Wrong value in dictionary")
#     if not len(users):
#         raise ValueError("Dictionary is empty")
#     users_by_name = sorted(users, key=get_user_name)
#     return users_by_name

# """Reading rows from file using list comprehension"""
#
#
# def read_file(file_name):
#     """Read file row after row"""
#
#     fread = open(file_name, "r")
#     data = [line for line in fread if line.startswith(">>")]
#     return data
#
# # print(read_file("log.txt"))

# """Processing big file using generator"""
#
#
# def read_file(file_name):
#     """Read file row after row"""
#
#     with open(file_name, "r") as fread:
#         for line in fread:
#             yield line
#
#
# for line in read_file("log.txt"):
#     if line.startswith(">>"):
#         print(line)
