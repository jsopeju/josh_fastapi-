from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Customer(Base):


    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(Boolean)
    gender = Column(String)
    country = Column(String)
    product_bought = Column(String)
    price_bought = Column(Integer)
    mobile_number = Column(Integer)
    rank = Column(String)


class   Designer(Base):


    __tablename__ = 'Designers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(Boolean)
    gender = Column(String)
    country = Column(String)
    product_sold = Column(String)
    price_sold = Column(Integer)
    mobile_number = Column(Integer)
    rank = Column(String)


class   Complaint(Base):


    __tablename__ = 'Complaints'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)
    gender = Column(String)
    country = Column(String)
    product_boughtt = Column(String)
    price_boughtt = Column(String)
    mobile_number = Column(Integer)
    rank = Column(String)
