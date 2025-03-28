from typing  import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.responses import RedirectResponse
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..rep import product

router = APIRouter(
    prefix= '/product',
    tags= ['Products']
)



@router.post('/')
def add_prodouct(insert: schemas.Product, db: Session = Depends(database.get_db)):
    return product.add_product(insert, db)
    

@router.get('/', response_model=List[schemas.Product])
def get_products(db: Session = Depends(database.get_db)):
    products = db.query(models.Product).all()
    return products


@router.get('/name', status_code=200, response_model=schemas.Product)
def get_product(name, respone: Response, db: Session = Depends(database.get_db)):
    return product.get_a_product(name, respone, db)

@router.put('/name', status_code=status.HTTP_202_ACCEPTED)
def update_product(name: str, request: schemas.Customer, db: Session = Depends(database.get_db)):
    return product.update_product(name, request, db)

@router.delete('/name', status_code=status.HTTP_204_NO_CONTENT)
def del_product(name: str, db: Session =  Depends(database.get_db)):
    return product.eliminate_product(name, db)
