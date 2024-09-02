from typing  import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.responses import RedirectResponse
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..rep import customer

router = APIRouter(
    prefix= '/customer',
    tags= ['Customers']
)



@router.post('/')
def create_user(insert: schemas.Customer, db: Session = Depends(database.get_db)):
    return customer.create(insert, db)
    

@router.get('/', response_model=List[schemas.GetUser])
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.Customer).all()
    return users


@router.get('/email', status_code=200, response_model=schemas.GetUser)
def get_user(email, respone: Response, db: Session = Depends(database.get_db)):
    return customer.get_a_user(email, respone, db)

@router.put('/email', status_code=status.HTTP_202_ACCEPTED)
def update_user(email: str, request: schemas.Customer, db: Session = Depends(database.get_db)):
    return customer.update(email, request, db)

@router.delete('/email', status_code=status.HTTP_204_NO_CONTENT)
def del_user(email: str, db: Session =  Depends(database.get_db)):
    return customer.eliminate(email, db)
