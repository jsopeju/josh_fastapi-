from fastapi import FastAPI, Depends, status, Response, HTTPException
from .router import authentication, auth, complaint, customer, designer
from . import  models
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(auth.router)
app.include_router(complaint.router)
app.include_router(customer.router)
app.include_router(designer.router)