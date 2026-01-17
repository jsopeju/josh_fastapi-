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
    designer_category: str
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

class Product(BaseModel):
    id: int
    product_name: str
    product_description: str
    product_price: str
    product_shipping_price: int
    product_colour: str
    product_size: str
    product_category: str
    product_designer: str
    

class Signin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


