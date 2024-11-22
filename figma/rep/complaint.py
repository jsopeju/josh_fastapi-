from sqlalchemy.orm import Session
from fastapi import HTTPException,Response, status
from .. import schemas, models


def create(insert: schemas.Complaint, db: Session ):
    new_user = models.Complaint(name=insert.name,email=insert.email,message=insert.message,gender=insert.gender,country=insert.country,product_bought=insert.product_bought,
                                price_bought=insert.price_bought,mobile_number=insert.mobile_number,rank=insert.rank)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    
    return new_user
    

def get_a_user(email: str, response: Response, db: Session):
    customer = db.query(models.Complaint).filter(models.Complaint.email == email).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Complaint with email {email} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    return customer

def update(email: str, request: schemas.Complaint, db: Session):
     customer = db.query(models.Complaint).filter(models.Complaint.email == email)
     if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Complaint with email {email} doesn't exist")
     customer.update(request)

     db.commit()

     return 'Details successfully updated...'

def eliminate(email: str, db: Session):
     blog = db.query(models.Complaint).filter(models.Complaint.email == email)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Complaint with email {email} doesn't exist")
     blog.delete(synchronize_session=False)
    
     db.commit()

     return 'Complaint successfully deleted'


