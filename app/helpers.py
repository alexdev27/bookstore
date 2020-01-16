from starlette.exceptions import HTTPException as StarletteHTTPexception
from fastapi import HTTPException
from app import app

# from typing import

def _proper_http_exception_format():
    """ для нормального форматирования для выдачи в апи"""


# @app.exception_handler(StarletteHTTPexception)
def raise_http_exception(exec_str: str, s_code: int = 400):


    raise HTTPException()
