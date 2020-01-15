
from .schemas import CreatedOrderResponse
from starlette.status import HTTP_201_CREATED

doc_create_order = dict(
    response_model=CreatedOrderResponse,
    description='Create Order!',
    summary='Create Order!!!',
    status_code=HTTP_201_CREATED,
    response_description='Order is created!',
)

