from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, JWT_Token
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags= ['Auth']

)


@router.post('/Login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Designer).filter(models.Designer.email == request.username).first() 
            
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid details" )
    
    if Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid details" )
               
    
    access_token = JWT_Token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "Signed in successfully...."}


@router.post("/Logout")
def logout():
    return  "Signed out successfully...."
