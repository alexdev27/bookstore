from fastapi import FastAPI, Query, Path
from mongoengine import connect
from fastapi.openapi.utils import get_openapi
from .book.schemas import InternalAppErrorResponse

app = FastAPI()
conn = connect(db='BooksStore', host='127.0.0.1', port=27017)

from .book import views


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Book Store",
        description="Test Project with docs",
        version="2.5.0",
        routes=app.routes,
    )
    _schema = InternalAppErrorResponse.schema()
    openapi_schema.setdefault('components', {})\
                    .setdefault('schemas', {})\
                    .setdefault(_schema['title'], _schema)
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
