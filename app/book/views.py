
from .doc_kwargs import doc_create_order
from .schemas import BookSchema, ResponseSchema
from app import app
from typing import List, Dict
from fastapi import Query, Path
from fastapi import HTTPException

base_route = '/books'


def _url(url: str = '') -> str:
    return f'{base_route}{url}'


# @app.get(_url('/{book_id}'))
# def get_book(book_id: str):
#     raise NotImplementedError('This function is not yet implemented')
#
#
# @app.get(_url(), response_model=List[BookSchema])
# def get_books():
#     raise NotImplementedError('This function is not yet implemented')


from pydantic import BaseModel, Field


def success(data: BaseModel):
    return {**data.dict()}

from fastapi import Query, Path
from .schemas import CreateOrderRequest

# @app.post(_url(), **doc_create_book)
# async def create_book(book: BookSchema):
#     return success(book)


@app.post(_url(), **doc_create_order)
def create_order(order: CreateOrderRequest):
    return success(order)

# @app.put(_url('/{book_id}'))
# def update_book():
#     raise NotImplementedError('This function is not yet implemented')
#
#
# @app.delete(_url('/{book_id}'), description='Delete book by ID')
# def delete_book():
#     raise NotImplementedError('This function is not yet implemented')
