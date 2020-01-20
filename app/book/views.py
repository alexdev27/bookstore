
from .doc_kwargs import doc_create_book
from .schemas import BookSchemaResponse, BookSchemaRequest, InternalAppErrorResponse
from app import app
from fastapi import HTTPException
from starlette.requests import Request

from pprint import pprint as pp
base_route = '/books'


def _url(url: str = '') -> str:
    return f'{base_route}{url}'


def failure(errs):
    return {'error': True, 'data': errs}


from starlette.responses import JSONResponse

from starlette.exceptions import HTTPException as StarletteHTTPException

from typing import List, Union, Dict

from typing import Union


class AppException(Exception):
    def __init__(self, data: Union[List[str], str], s_code: int = 400):
        self.status_code = s_code
        self.data: Dict[str, Union[List[str], str]] = InternalAppErrorResponse(data=data).dict()


def handle_err(req: Request, exc: AppException):
    return JSONResponse(content=exc.data, status_code=exc.status_code)


app.add_exception_handler(AppException, handle_err)


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc: HTTPException):
#     return JSONResponse(exc.detail, status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     errs = exc.errors()
#     formatted_err_list = []
#     for err in errs:
#         err_field = err['loc'][-1]
#         msg = f"'{err_field}' {err['msg']}"
#         formatted_err_list.append(msg)
#
#     return JSONResponse(failure(formatted_err_list), status_code=400)



@app.post(_url(), **doc_create_book)
async def create_book(book: BookSchemaRequest):
    b = {**book.dict()}
    # raise AppException(data='OOPs!', s_code=400)
    return BookSchemaResponse(**b)


# @app.post(_url(), **doc_create_order)
# async def create_order(order_9: CreateOrderRequest):
#     raise_http_exception('Something went wrong!', 400)


def raise_http_exception(exec_struct: str, s_code: int):
    data = failure(exec_struct)
    raise HTTPException(status_code=s_code, detail=data)

