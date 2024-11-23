from sqlalchemy.orm import Session
from fastapi import HTTPException,Response, status
from .. import schemas, models
from ..hashing import Hash


def create(insert: schemas.Customer, db: Session ):
    new_user = models.Customer(name=insert.name,email=insert.email,password=Hash.encrypt(insert.password),gender=insert.gender,
                              country=insert.country,mobile_number=insert.mobile_number,rank=insert.rank)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    
    return new_user, "Signed up sucessfully..."
    

def get_a_user(email: str, response: Response, db: Session):
    customer = db.query(models.Customer).filter(models.Customer.email == email).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with email {email} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    return customer

def update(email: str, request: schemas.Customer, db: Session):
     customer = db.query(models.Customer).filter(models.Customer.email == email)
     if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with email {email} doesn't exist")
     customer.update(request)

     db.commit()

     return  'Details successfully updated'

def eliminate(email: str, db: Session):
     blog = db.query(models.Customer).filter(models.Customer.email == email)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with email {email} doesn't exist")
     blog.delete(synchronize_session=False)
    
     db.commit()

     return {'detail': 'Customer successfully deleted'}


