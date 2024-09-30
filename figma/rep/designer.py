from sqlalchemy.orm import Session
from fastapi import HTTPException,Response, status
from .. import schemas, models
from ..hashing import Hash

def create(insert: schemas.Designer, db: Session ):
    new_user = models.Designer(name=insert.name,email=insert.email,password=Hash.encrypt(insert.password),gender=insert.gender,
                              country=insert.country,product_sold=insert.product_sold,mobile_number=insert.mobile_number,rank=insert.rank)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    
    return new_user, "Signed up sucessfully"
    

def get_a_designer(email: str, response: Response, db: Session):
    designer = db.query(models.Designer).filter(models.Designer.email == email).first()
    if not designer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Designer with email {email} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    return designer

def update(email: str, request: schemas.Designer, db: Session):
     designer = db.query(models.Designer).filter(models.Designer.email == email)
     if not designer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Designer with email {email} doesn't exist")
     designer.update(request)

     db.commit()

     return  'Details successfully updated'

def eliminate(email: str, db: Session):
     designer = db.query(models.Designer).filter(models.Designer.email == email)
     if not designer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Designer with email {email} doesn't exist")
     designer.delete(synchronize_session=False)
    
     db.commit()

     return {'detail': 'Designer successfully deleted'}
