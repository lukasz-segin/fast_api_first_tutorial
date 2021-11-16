from enum import Enum
# from fastapi import FastAPI


class BookCategory(str, Enum):
    cryminal = "kryminał"
    sensation = "sensacja"
    sci_fi = "science-fiction"
    fantasy = "fantasy books"


# app = FastAPI()
#
#
# @app.get("/books/{category_name}")
# async def book_category_description(category_name: BookCategory):
#     if category_name == BookCategory.sci_fi:
#         return {"category_name": category_name}
