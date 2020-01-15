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

from typing import Dict
from datetime import datetime


class ResponseSchema(BaseModel):
    error: bool
    msg: str
    data: BaseModel = None


class BookSchema(BaseModel):
    id: str
    name: str
    description: str



from pprint import pprint as pp
from enum import IntEnum, Enum


class PaymentTypeEnum(IntEnum):
    cash = 0
    noncash = 1


class DocumentTypesEnum(IntEnum):
    payment = 2
    return_order = 3
    insert = 4
    remove = 5


class OrderStatusEnum(IntEnum):
    ordered = 0
    payed = 1
    in_process = 2
    part_ready = 3
    order_ready = 4
    to_client = 5
    ready_cashier = 6
    canceled = 8


class CreateOrderRequest(BaseModel):
    on_site: bool = Field(..., title='Индикатор "На месте" или "С собой"')
    cart_id: str = Field(..., title='ID корзины с товарами из заказа')
    order_status: OrderStatusEnum = Field(..., title='Статус заказа')
    cash_client_order_id: str = Field(..., title='ID заказа (в системе Cashbox)', min_length=3)
    pay_type: PaymentTypeEnum = Field(..., title='Тип оплаты (наличка или безналичка)')
    doc_type: DocumentTypesEnum = Field(..., title='Тип документа (Оплата или Возврат)')
    pay_link: str = Field("", title='Ссылка платежа, если совершен безнал')
    cashier_name: str = Field(..., title='Имя кассира', min_length=3)
    device_id: str = Field(..., title='ID устройства на котором совершена оплата', min_length=3)
    cheque_number: PositiveInt = Field(..., title='Номер оплаченного заказа')
    cash_character: str = Field(..., title='Символ кассы (для отображения в интерфейсе)', min_length=1)
    order_time: datetime = Field(..., title='Время созданного заказа')


class CreatedOrderResponse(BaseModel):
    on_site: bool = Field(..., title='Индикатор "На месте" или "С собой"')
    order_status: OrderStatusEnum = Field(..., title='Статус заказа')
    cheque_number: PositiveInt = Field(..., title='Номер оплаченного заказа')
    cashier_name: str = Field(..., title='Имя кассира', min_length=3)
    order_time: datetime = Field(..., title='Время созданного заказа')
    pay_type: PaymentTypeEnum = Field(..., title='Тип оплаты (наличка или безналичка)')
    doc_type: DocumentTypesEnum = Field(..., title='Тип документа (Оплата или Возврат)')
