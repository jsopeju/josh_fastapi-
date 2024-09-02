from typing  import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.responses import RedirectResponse
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..rep import complaint

router = APIRouter(
    prefix= '/complaint',
    tags= ['Complaints']
)



@router.post('/')
def create_user_complain(insert: schemas.Complaint, db: Session = Depends(database.get_db)):
    return complaint.create(insert, db)
    

@router.get('/', response_model=List[schemas.GetUser])
def get_users_complains(db: Session = Depends(database.get_db)):
    users = db.query(models.Complaint).all()
    return users


@router.get('/email', status_code=200, response_model=schemas.GetUser)
def get_user_complain(email, respone: Response, db: Session = Depends(database.get_db)):
    return complaint.get_a_user(email, respone, db)

@router.put('/email', status_code=status.HTTP_202_ACCEPTED)
def update_user_complain(email: str, request: schemas.Complaint, db: Session = Depends(database.get_db)):
    return complaint.update(email, request, db)

@router.delete('/email', status_code=status.HTTP_204_NO_CONTENT)
def del_user_complain(email: str, db: Session =  Depends(database.get_db)):
    return complaint.eliminate(email, db)
