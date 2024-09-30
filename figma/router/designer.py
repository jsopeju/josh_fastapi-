from typing  import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.responses import RedirectResponse
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..rep import designer

router = APIRouter(
    prefix= '/designer',
    tags= ['Designers']
)



@router.post('/')
def create_designer(insert: schemas.Designer, db: Session = Depends(database.get_db)):
    return designer.create(insert, db)
    

@router.get('/', response_model=List[schemas.GetUser])
def get_designers(db: Session = Depends(database.get_db)):
    users = db.query(models.Designer).all()
    return users


@router.get('/email', status_code=200, response_model=schemas.GetUser)
def get_designer(email, respone: Response, db: Session = Depends(database.get_db)):
    return designer.get_a_designer(email, respone, db)

@router.put('/email', status_code=status.HTTP_202_ACCEPTED)
def update_desiger(email: str, request: schemas.Designer, db: Session = Depends(database.get_db)):
    return designer.update(email, request, db)

@router.delete('/email', status_code=status.HTTP_204_NO_CONTENT)
def del_designer(email: str, db: Session =  Depends(database.get_db)):
    return designer.eliminate(email, db)
