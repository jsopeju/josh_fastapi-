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
def create_prodouct(insert: schemas.Product, db: Session = Depends(database.get_db)):
    return product.create(insert, db)
    

@router.get('/', response_model=List[schemas.Product])
def get_products(db: Session = Depends(database.get_db)):
    users = db.query(models.Product).all()
    return users


@router.get('/name', status_code=200, response_model=schemas.Product)
def get_product(name, respone: Response, db: Session = Depends(database.get_db)):
    return product.get_a_user(name, respone, db)

@router.put('/name', status_code=status.HTTP_202_ACCEPTED)
def update_product(name: str, request: schemas.Customer, db: Session = Depends(database.get_db)):
    return product.update(name, request, db)

@router.delete('/name', status_code=status.HTTP_204_NO_CONTENT)
def del_product(name: str, db: Session =  Depends(database.get_db)):
    return product.eliminate(name, db)
