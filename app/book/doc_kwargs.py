
from .schemas import BookSchema
from starlette.status import HTTP_201_CREATED

doc_create_book = dict(
    response_model=BookSchema,
    description='Create book with name and description',
    summary='Create Book',
    status_code=HTTP_201_CREATED,
    response_description='Book is created!',
)

doc_get_book = dict(
    response_model=BookSchema
)

doc_update_book = dict(

)

doc_delete_book = dict(

)
