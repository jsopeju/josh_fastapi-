from pydantic import BaseModel
from typing import Optional
from pydantic.types import conint

class Customer(BaseModel):
    id: int
    name: str
    email: str
    password: str
    gender: str
    country: str
    product_bought: str
    price_bought: str
    mobile_number: int
    rank: str

class GetUser(Customer):
    class Config():
        from_attribute = True

class Designer(BaseModel):
    id: int
    name: str
    email: str
    password: str
    gender: str
    country: str
    product_sold: str
    price_sold: str
    mobile_number: int
    rank: str

class GetUser(Designer):
    class Config():
        from_attribute = True


class Complaint(BaseModel):
    id: int
    name: str
    email: str
    message: str
    gender: str
    country: str
    product_bought: str
    price_bought: str
    mobile_number: int
    rank: str

class GetUser(Complaint):
    class Config():
        from_attribute = True

class Signin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


