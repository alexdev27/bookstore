from pydantic import (
    BaseModel,
    validator,
    Field,
    NegativeFloat,
    StrictBool,
    StrictStr,
    NegativeInt,
    PositiveFloat,
    PositiveInt,
    conbytes,
    condecimal,
    confloat,
    conint,
    conlist,
    constr
)

from fastapi import HTTPException

from bson import ObjectId


from typing import Dict, Union, List
from datetime import datetime


class BookSchema(BaseModel):
    name: str = Field(..., title='Название книги')
    description: str = Field(..., title='Описание книги')

    # @validator('name')
    # def val_name(cls, v):
    #     from .views import raise_http_exception, AppException
    #     raise AppException(data='Oops!', s_code=400)
        # raise_http_exception('wrong', 400)
        # raise HTTPException(400, 'Someting went wrong!')

class BookSchemaRequest(BookSchema):
    pass


class BookSchemaResponse(BookSchema):
    pass


# from pprint import pprint as pp
# from enum import IntEnum, Enum
#
#
# class PaymentTypeEnum(IntEnum):
#     cash = 0
#     noncash = 1
#
#
# class DocumentTypesEnum(IntEnum):
#     payment = 2
#     return_order = 3
#     insert = 4
#     remove = 5
#
#
# class OrderStatusEnum(IntEnum):
#     ordered = 0
#     payed = 1
#     in_process = 2
#     part_ready = 3
#     order_ready = 4
#     to_client = 5
#     ready_cashier = 6
#     canceled = 8
#
#
# class CreateOrderRequest(BaseModel):
#     on_site: bool = Field(..., title='Индикатор "На месте" или "С собой"')
#     cart_id: str = Field(..., title='ID корзины с товарами из заказа')
#     order_status: OrderStatusEnum = Field(..., title='Статус заказа')
#     cash_client_order_id: str = Field(..., title='ID заказа (в системе Cashbox)', min_length=3)
#     pay_type: PaymentTypeEnum = Field(..., title='Тип оплаты (наличка или безналичка)')
#     doc_type: DocumentTypesEnum = Field(..., title='Тип документа (Оплата или Возврат)')
#     pay_link: str = Field("", title='Ссылка платежа, если совершен безнал')
#     cashier_name: str = Field(..., title='Имя кассира', min_length=3)
#     device_id: str = Field(..., title='ID устройства на котором совершена оплата', min_length=3)
#     cheque_number: PositiveInt = Field(..., title='Номер оплаченного заказа')
#     cash_character: str = Field(..., title='Символ кассы (для отображения в интерфейсе)', min_length=1)
#     order_time: datetime = Field(..., title='Время созданного заказа')
#
#     # @validator('cart_id')
#     # def check_valid_ObjectId(cls, v):
#     #     if not ObjectId.is_valid(v):
#     #         raise HTTPException(status_code=404, detail=f"Корзина с ID '{v}' не найдена")
#
#
# class CreatedOrderResponse(BaseModel):
#     on_site: bool = Field(..., title='Индикатор "На месте" или "С собой"')
#     order_status: OrderStatusEnum = Field(..., title='Статус заказа')
#     cheque_number: PositiveInt = Field(..., title='Номер оплаченного заказа')
#     cashier_name: str = Field(..., title='Имя кассира', min_length=3)
#     order_time: datetime = Field(..., title='Время созданного заказа')
#     pay_type: PaymentTypeEnum = Field(..., title='Тип оплаты (наличка или безналичка)')
#     doc_type: DocumentTypesEnum = Field(..., title='Тип документа (Оплата или Возврат)')


class InternalAppErrorResponse(BaseModel):
    error: bool = Field(True, title='Что-то пошло не так. Например, не найден ID сущности в базе')
    errors: List[str] = Field(..., title='Описание ошибок')
