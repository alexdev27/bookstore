
from .schemas import BookSchemaResponse, InternalAppErrorResponse
from starlette.status import HTTP_201_CREATED
from fastapi.openapi.constants import REF_PREFIX

from devtools import debug

aa = InternalAppErrorResponse.schema()['title']
print(aa)
# debug(InternalAppErrorResponse.schema()['title'])

err_response = {
    '400': {
        'description': 'internal Application Error aka Bad Request',
        'content': {
            'application/json': {
                'schema': {
                    '$ref': f'{REF_PREFIX}{InternalAppErrorResponse.schema()["title"]}'
                }
            }
        }
    }
}

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
    responses=err_response
)
