
from .schemas import BookSchemaResponse
from starlette.status import HTTP_201_CREATED

# doc_create_order = dict(
#     response_model=CreatedOrderResponse,
#     description='Create Order!',
#     summary='Create Order!!!',
#     status_code=HTTP_201_CREATED,
#     response_description='Order is created!',
# )

doc_create_book = dict(
    response_model=BookSchemaResponse,
    description='Method to create book',
    summary='Create Book',
    status_code=HTTP_201_CREATED,
    response_description='Book is created!',
)