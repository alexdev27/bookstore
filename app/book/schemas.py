from pydantic import BaseModel


class BookSchema(BaseModel):
    name: str
    description: str

