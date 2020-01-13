
from .doc_kwargs import doc_create_book, doc_get_book
from .schemas import BookSchema
from app import app
from typing import List
from fastapi import Query, Path


base_route = '/books'


def _url(url: str = '') -> str:
    return f'{base_route}{url}'


@app.get(_url('/{book_id}'))
def get_book(book_id: str):
    raise NotImplementedError('This function is not yet implemented')


@app.get(_url(), response_model=List[BookSchema])
def get_books():
    raise NotImplementedError('This function is not yet implemented')


from pydantic import  BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


@app.post(_url(), **doc_create_book)
def create_book(
        book: BookSchema,
        item: Item,
        user: User

):
    return {**book.dict()}


@app.put(_url('/{book_id}'))
def update_book():
    raise NotImplementedError('This function is not yet implemented')


@app.delete(_url('/{book_id}'), description='Delete book by ID')
def delete_book():
    raise NotImplementedError('This function is not yet implemented')



