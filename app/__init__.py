from fastapi import FastAPI, Query, Path
from mongoengine import connect


app = FastAPI(
    title="Book Store",
    description="Test Project with docs"
)
conn = connect(db='BooksStore', host='127.0.0.1', port=27017)

from .book import views
