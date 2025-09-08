from sqlalchemy.orm import Session
from fastapi import HTTPException,Response, status
from .. import schemas, models



def add_product(insert: schemas.Product, db: Session ):
    new_product = models.Product(product_name=insert.product_name,product_description=insert.product_description, product_price=insert.product_price, product_colour=insert.product_color,
                                product_shippingw_price=insert.product_shipping_price, product_size=insert.product_size, product_category=insert.product_category, product_designer=insert.product_designer)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    
    return new_product, "Product added sucessfully..."
    

def get_a_product(name: str, response: Response, db: Session):
    product = db.query(models.Product).filter(models.Product.product_name == name).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with name {name} doesn't exist" )
       # respone.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog with id {id} doesn't exist"}

    return product

def update_product(name: str, request: schemas.Product, db: Session):
     product = db.query(models.Product).filter(models.Product.product_name == name)
     if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with name {name} doesn't exist")
     product.update(request)

     db.commit()

     return  'Product details successfully updated'

def eliminate_product(name: str, db: Session):
     blog = db.query(models.Product).filter(models.Product.product_name == name)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with name {name} doesn't exist")
     blog.delete(synchronize_session=False)
    
     db.commit()

     return  'Product successfully deleted'


